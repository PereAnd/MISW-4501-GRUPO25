import functools
import http
import logging
from datetime import datetime
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)


class StateChoices:
    OPEN = "open"
    CLOSED = "closed"
    HALF_OPEN = "half_open"


class RemoteCallFailedException(Exception):
    pass


class CircuitBreaker:
    def __init__(self, exceptions, threshold, delay):
        """
        :param func: method that makes the remote call
        :param exceptions: an exception or a tuple of exceptions to catch (ideally should be network exceptions)
        :param threshold: number of failed attempts before the state is changed to "Open"
        :param delay: delay in seconds between "Closed" and "Half-Open" state
        """
        self.exceptions_to_catch = exceptions
        self.threshold = threshold
        self.delay = delay

        # by default set the state to closed
        self.state = StateChoices.CLOSED


        self.last_attempt_timestamp = None
        # keep track of failed attemp count
        self._failed_attempt_count = 0

    def update_last_attempt_timestamp(self):
        self.last_attempt_timestamp = datetime.utcnow().timestamp()

    def set_state(self, state):
        prev_state = self.state
        self.state = state
        logging.info(f"Changed state from {prev_state} to {self.state}")

    def handle_closed_state(self, *args, **kwargs):
        allowed_exceptions = self.exceptions_to_catch
        try:
            ret_val = self.func(*args, **kwargs)
            logging.info("Success: Remote call")
            self.update_last_attempt_timestamp()
            return ret_val
        except allowed_exceptions as e:
            # remote call has failed
            logging.info("Failure: Remote call")
            # increment the failed attempt count
            self._failed_attempt_count += 1

            # update last_attempt_timestamp
            self.update_last_attempt_timestamp()

            # if the failed attempt count is more than the threshold
            # then change the state to OPEN
            if self._failed_attempt_count >= self.threshold:
                self.set_state(StateChoices.OPEN)
            # re-raise the exception
            #raise RemoteCallFailedException from e
            return "El backend no está disponible", 503

    def handle_open_state(self, *args, **kwargs):
        current_timestamp = datetime.utcnow().timestamp()
        # if `delay` seconds have not elapsed since the last attempt, raise an exception
        if self.last_attempt_timestamp + self.delay >= current_timestamp:
            return f"El backend no está disponible, reintente luego de {self.last_attempt_timestamp+self.delay-current_timestamp} segundos", 503
            #raise RemoteCallFailedException(f"Retry after {self.last_attempt_timestamp+self.delay-current_timestamp} secs")

        # after `delay` seconds have elapsed since the last attempt, try making the remote call
        # update the state to half open state
        self.set_state(StateChoices.HALF_OPEN)
        allowed_exceptions = self.exceptions_to_catch
        try:
            ret_val = self.func(*args, **kwargs)
            # the remote call was successful
            # now reset the state to Closed
            self.set_state(StateChoices.CLOSED)
            # reset the failed attempt counter
            self._failed_attempt_count = 0
            # update the last_attempt_timestamp
            self.update_last_attempt_timestamp()
            # return the remote call's response
            return ret_val
        except allowed_exceptions as e:
            # the remote call failed again
            # increment the failed attempt count
            self._failed_attempt_count += 1

            # update last_attempt_timestamp
            self.update_last_attempt_timestamp()

            # set the state to "OPEN"
            self.set_state(StateChoices.OPEN)

            # raise the error
            return "El backend no está disponible", 503
            #raise RemoteCallFailedException from e

    def make_remote_call(self,  *args, **kwargs):
        if self.state == StateChoices.CLOSED:
            return self.handle_closed_state(*args, **kwargs)
        if self.state == StateChoices.OPEN:
            return self.handle_open_state(*args, **kwargs)



    def valid_response(self, url, response):
        if 500 <= response.status_code < 600:
            print(f"Call to {url} failed with status code = {response.status_code}")
            raise Exception("Server Issue")
        else:
            print(f"Call to {url} succeed with status code = {response.status_code}")
            if response.status_code == 204:
                return response.text, response.status_code    
            else:
                return response.json(), response.status_code

    def make_get(self, url, params=None):
        try:
            response = requests.get(url, params=params,timeout=1)
            return self.valid_response(url, response)
        except Exception:
            print(f"Call to {url} failed")
            raise


    def make_patch(self, url, json=None):
        try:
            response = requests.patch(url, json=json,timeout=1)
            return self.valid_response(url, response)
        except Exception:
            print(f"Call to {url} failed")
            raise

    def make_post(self, url, json=None):
        try:
            response = requests.post(url, json=json,timeout=1)
            return self.valid_response(url, response)
        except Exception:
            print(f"Call to {url} failed")
            raise

    def make_delete(self, url, json=None):
        try:
            response = requests.delete(url,timeout=1)
            return self.valid_response(url, response)
        except Exception:
            print(f"Call to {url} failed")
            raise

    def make_remote_call_get(self, url, params=None):
        self.func = self.make_get
        return self.make_remote_call(url, params=params)

        
    def make_remote_call_patch(self, url, json=None):
        self.func = self.make_patch
        return self.make_remote_call(url, json=json)

    def make_remote_call_post(self,url, json=None):
        self.func = self.make_post
        return self.make_remote_call(url, json=json)

    def make_remote_call_delete(self,url):
        self.func = self.make_delete
        return self.make_remote_call(url, json=None)

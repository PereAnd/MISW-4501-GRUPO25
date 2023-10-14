import pytest
from flask.testing import FlaskClient
from src.app import app, db
from src.modelos import Publicacion
import requests
import os
GU_URL_V = str(os.getenv("GU_URL"))
url_test = GU_URL_V + '/users/'
url_test_auth = GU_URL_V + '/users/auth'

@pytest.fixture
def client():
    #Usuario.query.delete()
    #db.session.commit()
    return app.test_client()


def test_user_create(client: FlaskClient):
    json={'username': 'cesa96','password': 'passwordCesa96','email': 'cesa96@gmail.com'}
    
    response = requests.post(url_test, json=json)
    jsonreponse = response.json()

    if response.status_code == 200:
        assert jsonreponse["id"]
    else:
        assert response.status_code == 412

def test_publication_create(client: FlaskClient):
    json={'username': 'cesa96','password': 'passwordCesa96'}
    response = requests.post(url_test_auth, json=json)

    assert response.status_code == 200
    jsonreponse = response.json()

    token = jsonreponse["token"]
    tokenG = token

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.post(
        '/posts/', json={'routeId': 1,'plannedStartDate': '02/19/23 14:55:26','plannedEndDate': '04/19/23 13:55:26'})
    assert resp.status_code == 201
    assert resp.json.get('id')

def test_publication_create_token_not_valid(client: FlaskClient):
    tokenG = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3NjE3NjU4MSwianRpIjoiYzg5NGVhY2UtYWQ5NC00NDhmLTliMmMtMzhlZmRhN2NlODM4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IkJyYXlhbiIsIm5iZiI6MTY3NjE3NjU4MSwiZXhwIjoxNjc2MTc2ODgxfQ.TRR_Hkf7U0bIF7xad0V_7UZiA83myo_5GoObFLio2sE'

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.post(
        '/posts/', json={'routeId': 1,'plannedStartDate': '02/19/23 14:55:26','plannedEndDate': '04/19/23 13:55:26'})
    assert resp.status_code == 401

def test_publication_create_data_incompleted(client: FlaskClient):
    json={'username': 'cesa96','password': 'passwordCesa96'}
    response = requests.post(url_test_auth, json=json)

    assert response.status_code == 200
    jsonreponse = response.json()

    token = jsonreponse["token"]
    tokenG = token

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.post(
        '/posts/', json={'routeId': 1,'plannedStartDate': '02/19/23 14:55:26'})
    assert resp.status_code == 400

def test_publication_create_data_invalid(client: FlaskClient):
    json={'username': 'cesa96','password': 'passwordCesa96'}
    response = requests.post(url_test_auth, json=json)

    assert response.status_code == 200
    jsonreponse = response.json()

    token = jsonreponse["token"]
    tokenG = token

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.post(
        '/posts/', json={'routeId': 1,'plannedStartDate': '02/19/23 14:55:26','plannedEndDate': '24/19/23 13:55:26'})
    assert resp.status_code == 412

def test_find_publication(client: FlaskClient):
    json={'username': 'cesa96','password': 'passwordCesa96'}
    response = requests.post(url_test_auth, json=json)

    assert response.status_code == 200
    jsonreponse = response.json()

    token = jsonreponse["token"]
    tokenG = token

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.get(
        '/posts?route=1&filter=me&when=02-19-23 14:55:26')
    assert resp.status_code == 200

def test_find_publication_data_invalid(client: FlaskClient):
    json={'username': 'cesa96','password': 'passwordCesa96'}
    response = requests.post(url_test_auth, json=json)

    assert response.status_code == 200
    jsonreponse = response.json()

    token = jsonreponse["token"]
    tokenG = token

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.get(
        '/posts?when=260')
    assert resp.status_code == 400

def test_find_publication_token_invalid(client: FlaskClient):
    tokenG = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3NjE3NjU4MSwianRpIjoiYzg5NGVhY2UtYWQ5NC00NDhmLTliMmMtMzhlZmRhN2NlODM4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IkJyYXlhbiIsIm5iZiI6MTY3NjE3NjU4MSwiZXhwIjoxNjc2MTc2ODgxfQ.TRR_Hkf7U0bIF7xad0V_7UZiA83myo_5GoObFLio2sE'

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.get(
        '/posts?when=260')
    assert resp.status_code == 401

def test_query_publication(client: FlaskClient):
    json={'username': 'cesa96','password': 'passwordCesa96'}
    response = requests.post(url_test_auth, json=json)

    assert response.status_code == 200
    jsonreponse = response.json()

    token = jsonreponse["token"]
    tokenG = token

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.get(
        '/posts/1')
    assert resp.status_code == 200

def test_query_publication_token_invalid(client: FlaskClient):
    tokenG = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3NjE3NjU4MSwianRpIjoiYzg5NGVhY2UtYWQ5NC00NDhmLTliMmMtMzhlZmRhN2NlODM4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IkJyYXlhbiIsIm5iZiI6MTY3NjE3NjU4MSwiZXhwIjoxNjc2MTc2ODgxfQ.TRR_Hkf7U0bIF7xad0V_7UZiA83myo_5GoObFLio2sE'

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.get(
        '/posts/1')
    assert resp.status_code == 401

def test_query_publication_data_invalid(client: FlaskClient):
    json={'username': 'cesa96','password': 'passwordCesa96'}
    response = requests.post(url_test_auth, json=json)

    assert response.status_code == 200
    jsonreponse = response.json()

    token = jsonreponse["token"]
    tokenG = token

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.get(
        '/posts/hola')
    assert resp.status_code == 400

def test_query_publication_data_no_exists(client: FlaskClient):
    json={'username': 'cesa96','password': 'passwordCesa96'}
    response = requests.post(url_test_auth, json=json)

    assert response.status_code == 200
    jsonreponse = response.json()

    token = jsonreponse["token"]
    tokenG = token

    client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + tokenG
    resp = client.get(
        '/posts/5')
    assert resp.status_code == 404

def test_ping_publication(client: FlaskClient):
    resp = client.get(
        '/posts/ping/')
    assert resp.status_code == 200

    
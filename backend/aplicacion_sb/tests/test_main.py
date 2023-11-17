import pytest
from flask.testing import FlaskClient
from src.app import app
import requests
import os, time
from faker import Faker
fake = Faker()

id_empresa = 0
id_proyecto = 0
id_perfil = 0
id_candidato = 0
id_aplicacion = 0
id_entrevista = 0
name = ''
urlBackEndEmpr = str(os.getenv("EMPR_BACK_URL")) + "/empresa"
urlBackEndPerf = str(os.getenv("PERF_BACK_URL")) + "/empresa"
urlBackEndCand = str(os.getenv("CAND_BACK_URL")) + "/candidato"


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
# Crea una empresa y un proyecto
    global id_empresa, urlBackEnd, id_proyecto

@pytest.fixture
def client():
    #Usuario.query.delete()
    #db.session.commit()
    return app.test_client()

# Pruebas perfiles
def test_crea_aplicacion(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion

    resp = requests.post(
        urlBackEndEmpr, json={'name': fake.name(),'mail': fake.email(),'password': 'prueba1','confirmPassword': 'prueba1'})
    jsonReponse = resp.json()
    assert resp.status_code == 201
    id_empresa = jsonReponse["id"]
    resp = requests.post(
        urlBackEndEmpr + "/" + str(id_empresa) + "/proyecto", json={'proyecto': "prueba",'description': 'prueba'})
    
    assert resp.status_code == 201
    jsonReponse = resp.json()
    id_proyecto = jsonReponse['id']

    resp = requests.post(
        urlBackEndPerf + "/" + str(id_empresa) + "/proyecto/" + str(id_proyecto) + "/perfil", json={'name': 'prueba','role': 'prueba','location': fake.city(),'years': fake.random_int(0, 40)})
    
    assert resp.status_code == 201
    jsonReponse = resp.json()
    id_perfil = jsonReponse['id']

    resp = requests.post(
        urlBackEndCand, json={'names': fake.name(),'lastNames': fake.name(),'mail': fake.email(),'password': 'prueba1','confirmPassword': 'prueba1'})
    
    assert resp.status_code == 201
    jsonReponse = resp.json()
    id_candidato = jsonReponse['id']


    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion" , json={'applicationDate': '1978-03-15T00:00:00.000Z','status': 'NEW', 'candidatoId':id_candidato})
    assert resp.status_code == 201


    assert resp.json.get('id')    
    id_aplicacion = resp.json.get('id')

def test_crea_aplicacion_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion

    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + "/aplicacion" , json={'applicationDate': '1978-03-15T00:00:00.000Z','status': 'NEW', 'candidatoId':id_candidato})
    assert resp.status_code == 404

    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion" , json={'applicationDate': '1978-03-15T00:00:00.000Z','status': 'NEW', 'candidatoId':'123dd'})
    assert resp.status_code == 400

    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion" , json={'applicationDate': '1978-03-15T00:00:00.000Z','status': 'NEW', 'candidatoId':'1234'})
    assert resp.status_code == 404

    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion" , json={'applicationDate': '','status': 'NEW', 'candidatoId':id_candidato})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion" , json={'status': 'NEW', 'candidatoId':id_candidato})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion" , json={'applicationDate': '1978-20-15T00:00:00.000Z','status': 'NEW', 'candidatoId':id_candidato})
    assert resp.status_code == 400


def test_actualiza_aplicacion(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion, name

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion/" + str(id_aplicacion), json={'applicationDate': '1978-04-15T00:00:00.000Z','status': 'CANCEL'})
    assert resp.status_code == 200
    assert resp.json.get('status') == 'CANCEL'


def test_actualiza_aplicacion_id_no_numeric(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    name = fake.words(2)
    description = fake.words(6)
    role = fake.words(2)
    location = fake.city()
    years = fake.random_int(0, 40)
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion/" + 'dddd', json={'name': name,'applicationDate': '1978-04-15T00:00:00.000Z', 'status':'CANCEL'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' 'dddd' + "/aplicacion/" + str(id_aplicacion), json={'name': name,'applicationDate': '1978-04-15T00:00:00.000Z', 'status':'CANCEL'})
    assert resp.status_code == 400


def test_actualiza_aplicacion_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion/" + str(id_aplicacion), json={'applicationDate': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion/" + str(id_aplicacion), json={'applicationDate': '1978-14-15T00:00:00.000Z'})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion/" + str(id_aplicacion), json={'status': ''})
    assert resp.status_code == 400

def test_obtiene_aplicaciones(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion")
    assert resp.status_code == 200

def test_obtiene_aplicaciones_id_incorrecto(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + 'ddddd' + "/aplicacion")
    assert resp.status_code == 400


def test_obtiene_aplicaciones_id(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion, name
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + "/perfil/" + str(id_perfil)+ "/aplicacion/" + str(id_aplicacion))
    assert resp.status_code == 200

def test_obtiene_aplicaciones_id_incorrecto(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion, name
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + "/perfil/" + str(id_perfil)+ "/aplicacion/" + 'ddddd')
    assert resp.status_code == 400

    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + "/perfil/" + str(id_perfil)+ "/aplicacion/" + '1234')
    assert resp.status_code == 404

    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + "/perfil/" + 'dddd' + "/aplicacion/"  + str(id_aplicacion))
    assert resp.status_code == 400


def test_elimina_aplicacion_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/aplicacion/' + str(id_aplicacion))
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + '1234')
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/44444/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion))
    assert resp.status_code == 404

# Pruebas Entrevista

def test_crea_entrevista(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista', json={'enterviewDate': "1978-03-15T00:00:00.000Z",'done': False, 'feedback': 'Prueba Feedback'})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_entrevista = resp.json.get('id')

def test_crea_entrevista_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista', json={'enterviewDate': "1978-13-15T00:00:00.000Z",'done': False, 'feedback': 'Prueba Feedback'})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista', json={'enterviewDate': "1978-03-15T00:00:00.000Z",'done': 'jjjj', 'feedback': 'Prueba Feedback'})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista', json={'enterviewDate': "1978-03-15T00:00:00.000Z",'done': False})
    assert resp.status_code == 201
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista', json={'enterviewDate': "1978-03-15T00:00:00.000Z",'done': False, 'feedback': ''})
    assert resp.status_code == 201


def test_crea_entrevista_aplicacion_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/12346/aplicacion/' + str(id_aplicacion) + '/entrevista',json={'enterviewDate': "1978-03-15T00:00:00.000Z",'done': False, 'feedback': 'Prueba Feedback'})
    assert resp.status_code == 404
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/hhhhhh/entrevista', json={'enterviewDate': "1978-03-15T00:00:00.000Z",'done': False, 'feedback': 'Prueba Feedback'})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/12345/perfil/' + str(id_perfil) + '/aplicacion/123131/entrevista', json={'enterviewDate': "1978-03-15T00:00:00.000Z",'done': False, 'feedback': 'Prueba Feedback'})
    assert resp.status_code == 404

def test_actualiza_entrevista(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + str(id_entrevista), json={'enterviewDate': "1978-04-15T00:00:00.000Z",'done': True, 'feedback': 'Prueba Feedback 2'})
    assert resp.status_code == 200
    assert resp.json.get('feedback') == 'Prueba Feedback 2'
    assert resp.json.get('done') == True
 
def test_actualiza_entrevista_id_no_numeric(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/ddddd/entrevista/' + str(id_entrevista), json={'enterviewDate': "1978-04-15T00:00:00.000Z",'done': True, 'feedback': 'Prueba Feedback 2'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + '5ddd', json={'enterviewDate': "1978-04-15T00:00:00.000Z",'done': True, 'feedback': 'Prueba Feedback 2'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/dddd/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + str(id_entrevista), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400


def test_actualiza_entrevista_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + '1234', json={'enterviewDate': "1978-04-15T00:00:00.000Z",'done': True, 'feedback': 'Prueba Feedback 2'})
    assert resp.status_code == 404
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + str(id_entrevista), json={'enterviewDate': "1978-04-15T00:00:00.000Z",'done': True, 'feedback': 'Prueba Feedback 2'})
    assert resp.status_code == 404
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + '1234' + '/entrevista/' + str(id_entrevista), json={'enterviewDate': "1978-04-15T00:00:00.000Z",'done': True, 'feedback': 'Prueba Feedback 2'})
    assert resp.status_code == 404

def test_actualiza_entrevista_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + str(id_entrevista), json={'enterviewDate': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + str(id_entrevista), json={'done': ''})
    assert resp.status_code == 400


def test_obtiene_entrevista(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista')
    assert resp.status_code == 200



def test_obtiene_entrevista_perfil_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + '1234' + '/entrevista')
    assert resp.status_code == 404

    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/1234/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista')
    assert resp.status_code == 404

def test_obtiene_entrevista_id(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + str(id_entrevista))
    assert resp.status_code == 200

def test_obtiene_entrevista_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + '3434' + '/entrevista/' + str(id_entrevista))
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + '1234')
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + '1234' + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + str(id_entrevista))
    assert resp.status_code == 404

def test_obtiene_aplicaciones_candidato(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.get(
        '/candidato/' + str(id_candidato) + "/aplicacion")
    assert resp.status_code == 200

def test_obtiene_aplicaciones_id_candidato(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion, name
    resp = client.get(
        '/candidato/' + str(id_candidato) + "/aplicacion/" + str(id_aplicacion))
    assert resp.status_code == 200


def test_obtiene_entrevista_candidato(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/aplicacion/' + str(id_aplicacion) + '/entrevista')
    assert resp.status_code == 200


def test_obtiene_entrevista_id_candidato(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + str(id_entrevista))
    assert resp.status_code == 200





def test_elimina_entrevista(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + str(id_entrevista))
    assert resp.status_code == 204

def test_elimina_entrevista_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + '3434' + '/entrevista/' + str(id_entrevista))
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + '1234')
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + '1234' + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion) + '/entrevista/' + str(id_entrevista))
    assert resp.status_code == 404


def test_elimina_aplicacion(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_entrevista, id_aplicacion
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/aplicacion/' + str(id_aplicacion))
    assert resp.status_code == 204








def test_circuit_breaker(client: FlaskClient):
    global id_empresa, id_informacion_tecnica
    tempEnv = os.environ["APLI_BACK_URL"]
    os.environ["APLI_BACK_URL"] = 'http://noexiste.com:5001'
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion")
    assert resp.status_code == 503
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion")
    assert resp.status_code == 503
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion")
    assert resp.status_code == 503
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion")
    assert resp.status_code == 503
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion")
    assert resp.status_code == 503
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion")
    assert resp.status_code == 503
    os.environ["APLI_BACK_URL"] = tempEnv   
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion")
    assert resp.status_code == 503

    time.sleep(10)
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/aplicacion")
    assert resp.status_code == 200

import pytest
from flask.testing import FlaskClient
from src.app import app, db
from src.modelos import Busqueda, Resultado
import requests
import os
from faker import Faker
fake = Faker()

id_empresa = 0
id_proyecto = 0
id_perfil = 0
id_candidato = 0
id_busqueda = 0
id_resultado = 0
id_conocimiento = 0
id_resultado = 0
id_idioma = 0
name = ''
urlBackEndEmpr = str(os.getenv("EMPR_BACK_URL")) + "/empresa"
urlBackEndPerf = str(os.getenv("PERF_BACK_URL")) + "/empresa"
urlBackEndCand = str(os.getenv("CAND_BACK_URL")) + "/candidato"


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
# Crea una empresa y un proyecto
    global id_empresa, urlBackEnd, id_proyecto

    Busqueda.query.delete()
    Resultado.query.delete()

@pytest.fixture
def client():
    #Usuario.query.delete()
    #db.session.commit()
    return app.test_client()

# Pruebas perfiles
def test_crea_busqueda(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda

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
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/busqueda")
    assert resp.status_code == 201


    assert resp.json.get('id')    
    id_busqueda = resp.json.get('id')

def test_crea_busqueda_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda

    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + "/busqueda" )
    assert resp.status_code == 404


def test_obtiene_busquedaes(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + "/busqueda")
    assert resp.status_code == 200

def test_obtiene_busquedaes_id_incorrecto(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + 'ddddd' + "/busqueda")
    assert resp.status_code == 400


def test_obtiene_busquedaes_id(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda, name
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + "/perfil/" + str(id_perfil)+ "/busqueda/" + str(id_busqueda))
    assert resp.status_code == 200

def test_obtiene_busquedaes_id_incorrecto(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda, name
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + "/perfil/" + str(id_perfil)+ "/busqueda/" + 'ddddd')
    assert resp.status_code == 400

    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + "/perfil/" + str(id_perfil)+ "/busqueda/" + '1234')
    assert resp.status_code == 404

    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + "/perfil/" + 'dddd' + "/busqueda/"  + str(id_busqueda))
    assert resp.status_code == 400


def test_elimina_busqueda_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/busqueda/' + str(id_busqueda))
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/' + '1234')
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/44444/perfil/' + str(id_perfil) + '/busqueda/' + str(id_busqueda))
    assert resp.status_code == 404

# Pruebas Resultado

def test_crea_resultado(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/' + str(id_busqueda) + '/resultado', json={'candidatoId': id_candidato})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_resultado = resp.json.get('id')

def test_crea_resultado_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/' + str(id_busqueda) + '/resultado', json={'candidatoId': ''})
    assert resp.status_code == 400

def test_crea_resultado_busqueda_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/12346/busqueda/' + str(id_busqueda) + '/resultado',json={'candidatoId': id_candidato})
    assert resp.status_code == 404
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/hhhhhh/resultado', json={'candidatoId': id_candidato})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/12345/perfil/' + str(id_perfil) + '/busqueda/123131/resultado', json={'candidatoId': id_candidato})
    assert resp.status_code == 404
 

def test_obtiene_resultado(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/' + str(id_busqueda) + '/resultado')
    assert resp.status_code == 200


def test_obtiene_resultado_perfil_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/' + '1234' + '/resultado')
    assert resp.status_code == 404

    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/1234/perfil/' + str(id_perfil) + '/busqueda/' + str(id_busqueda) + '/resultado')
    assert resp.status_code == 404

def test_obtiene_resultado_id(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/' + str(id_busqueda) + '/resultado/' + str(id_resultado))
    assert resp.status_code == 200


def test_elimina_resultado(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/' + str(id_busqueda) + '/resultado/' + str(id_resultado))
    assert resp.status_code == 204

def test_elimina_resultado_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/' + '3434' + '/resultado/' + str(id_resultado))
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/' + str(id_busqueda) + '/resultado/' + '1234')
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + '1234' + '/perfil/' + str(id_perfil) + '/busqueda/' + str(id_busqueda) + '/resultado/' + str(id_resultado))
    assert resp.status_code == 404


def test_elimina_busqueda(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_candidato, id_resultado, id_busqueda
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/busqueda/' + str(id_busqueda))
    assert resp.status_code == 204
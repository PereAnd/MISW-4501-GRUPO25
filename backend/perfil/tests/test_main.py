import pytest
from flask.testing import FlaskClient
from src.app import app, db
from src.modelos import Perfil, Habilidad, Conocimiento, Idioma
import requests
import os
from faker import Faker
fake = Faker()

id_empresa = 0
id_proyecto = 0
id_perfil = 0
id_conocimiento = 0
id_habilidad = 0
id_idioma = 0
name = ''
urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
# Crea una empresa y un proyecto
    global id_empresa, urlBackEnd, id_proyecto


    Habilidad.query.delete()
    Conocimiento.query.delete()
    Idioma.query.delete()
    Perfil.query.delete()

@pytest.fixture
def client():
    #Usuario.query.delete()
    #db.session.commit()
    return app.test_client()

# Pruebas perfiles
def test_registro_perfil(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto

    resp = requests.post(
        urlBackEnd, json={'name': fake.name(),'mail': fake.email(),'password': 'prueba1','confirmPassword': 'prueba1'})
    jsonReponse = resp.json()
    assert resp.status_code == 201
    id_empresa = jsonReponse["id"]
    resp = requests.post(
        urlBackEnd + "/" + str(id_empresa) + "/proyecto", json={'proyecto': "prueba",'description': 'prueba'})
    
    assert resp.status_code == 201
    jsonReponse = resp.json()
    id_proyecto = jsonReponse['id']

    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil', json={'name': 'prueba','role': 'prueba','location': fake.city(),'years': fake.random_int(0, 40)})
    assert resp.status_code == 201
    assert resp.json.get('id')    
    id_perfil = resp.json.get('id')

def test_registro_perfil_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil', json={'name': 'prueba','location': fake.city(),'years': fake.random_int(0, 40)})
    assert resp.status_code == 400  
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil', json={'name': fake.words(2),'role': '','location': fake.city(),'years': fake.random_int(0, 40)})
    assert resp.status_code == 400  

def test_actualiza_perfil(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, name

    name = fake.name()
    role = fake.name()
    location = fake.city()
    years = fake.random_int(0, 40)
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil), json={'name': name,'role': role, 'location':location,'years': years})
    assert resp.status_code == 200
    assert resp.json.get('name') == name
    assert resp.json.get('role') == role
    assert resp.json.get('location') == location
    assert resp.json.get('years') == years


def test_actualiza_perfil_id_no_numeric(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto
    name = fake.words(2)
    description = fake.words(6)
    role = fake.words(2)
    location = fake.city()
    years = fake.random_int(0, 40)
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/ddd', json={'name': name,'role': role, 'location':location,'years': years})
    assert resp.status_code == 400


def test_actualiza_perfil_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil), json={'name': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil), json={'role': '',})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil), json={'location': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil), json={'years': ''})
    assert resp.status_code == 400

def test_obtiene_perfiles(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil')
    assert resp.status_code == 200
    jsonreponse = resp.json
    #assert jsonreponse[0]['name'] == 'César'

def test_obtiene_perfiles_id(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, name
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + "/perfil/" + str(id_perfil))
    assert resp.status_code == 200
    assert resp.json.get('name') == name

# Pruebas Habilidad

def test_crea_habilidad(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad', json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_habilidad = resp.json.get('id')

def test_crea_habilidad_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad', json={'name': "Prueba Nombre"})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad', json={'name': "Prueba Nombre",'description': ''})
    assert resp.status_code == 400

def test_crea_habilidad_perfil_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/123456/habilidad',json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 404
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/dd444/habilidad', json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/12345/perfil/' + str(id_perfil) + '/habilidad', json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 404

def test_actualiza_habilidad(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad/' + str(id_habilidad), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 200
    assert resp.json.get('name') == 'Prueba Nombre 1'
    assert resp.json.get('description') == 'Prueba Description 1'
 
def test_actualiza_habilidad_id_no_numeric(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + 'dddd' + '/habilidad/' + str(id_habilidad), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad/' + '5ddd', json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/dddd/perfil/' + str(id_perfil) + '/habilidad/' + str(id_habilidad), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400


def test_actualiza_habilidad_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/habilidad/' + str(id_habilidad), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 404
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad/' + '1234', json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 404

def test_actualiza_habilidad_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad/' + str(id_habilidad), json={'name': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad/' + str(id_habilidad), json={'description': ''})
    assert resp.status_code == 400


def test_obtiene_habilidad(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad')
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['name'] == 'Prueba Nombre 1'


def test_obtiene_habilidad_perfil_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '123' + '/habilidad')
    assert resp.status_code == 404

    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/1234/perfil/' + str(id_perfil) + '/habilidad')
    assert resp.status_code == 404

def test_obtiene_habilidad_id(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad/' + str(id_habilidad))
    assert resp.status_code == 200
    assert resp.json.get('name') == 'Prueba Nombre 1'

def test_obtiene_habilidad_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/habilidad/' + str(id_habilidad))
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad/' + '1234')
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + '1234' + '/perfil/' + str(id_perfil) + '/habilidad/' + str(id_habilidad))
    assert resp.status_code == 404

def test_elimina_habilidad(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad/' + str(id_habilidad))
    assert resp.status_code == 204

def test_elimina_habilidad_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_habilidad
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/habilidad/' + str(id_habilidad))
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/habilidad/' + '1234')
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/44444/perfil/' + str(id_perfil) + '/habilidad/' + str(id_habilidad))
    assert resp.status_code == 404

# Pruebas Conocimiento

def test_crea_conocimiento(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento', json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_conocimiento = resp.json.get('id')

def test_crea_conocimiento_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento', json={'name': "Prueba Nombre"})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento', json={'name': "Prueba Nombre",'description': ''})
    assert resp.status_code == 400

def test_crea_conocimiento_perfil_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/123456/conocimiento',json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 404
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/dd444/conocimiento', json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/12345/perfil/' + str(id_perfil) + '/conocimiento', json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 404

def test_actualiza_conocimiento(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento/' + str(id_conocimiento), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 200
    assert resp.json.get('name') == 'Prueba Nombre 1'
    assert resp.json.get('description') == 'Prueba Description 1'
 
def test_actualiza_conocimiento_id_no_numeric(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + 'dddd' + '/conocimiento/' + str(id_conocimiento), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento/' + '5ddd', json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/dddd/perfil/' + str(id_perfil) + '/conocimiento/' + str(id_conocimiento), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400


def test_actualiza_conocimiento_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/conocimiento/' + str(id_conocimiento), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 404
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento/' + '1234', json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 404

def test_actualiza_conocimiento_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento/' + str(id_conocimiento), json={'name': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento/' + str(id_conocimiento), json={'description': ''})
    assert resp.status_code == 400


def test_obtiene_conocimiento(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento')
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['name'] == 'Prueba Nombre 1'


def test_obtiene_conocimiento_perfil_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '123' + '/conocimiento')
    assert resp.status_code == 404

    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/1234/perfil/' + str(id_perfil) + '/conocimiento')
    assert resp.status_code == 404

def test_obtiene_conocimiento_id(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento/' + str(id_conocimiento))
    assert resp.status_code == 200
    assert resp.json.get('name') == 'Prueba Nombre 1'

def test_obtiene_conocimiento_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/conocimiento/' + str(id_conocimiento))
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento/' + '1234')
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + '1234' + '/perfil/' + str(id_perfil) + '/conocimiento/' + str(id_conocimiento))
    assert resp.status_code == 404

def test_elimina_conocimiento(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento/' + str(id_conocimiento))
    assert resp.status_code == 204

def test_elimina_conocimiento_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_conocimiento
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/conocimiento/' + str(id_conocimiento))
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/conocimiento/' + '1234')
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/44444/perfil/' + str(id_perfil) + '/conocimiento/' + str(id_conocimiento))
    assert resp.status_code == 404

# Pruebas Idioma

def test_crea_idioma(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma', json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_idioma = resp.json.get('id')

def test_crea_idioma_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma', json={'name': "Prueba Nombre"})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma', json={'name': "Prueba Nombre",'description': ''})
    assert resp.status_code == 400

def test_crea_idioma_perfil_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/123456/idioma',json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 404
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/dd444/idioma', json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto/12345/perfil/' + str(id_perfil) + '/idioma', json={'name': "Prueba Nombre",'description': 'Prueba Description'})
    assert resp.status_code == 404

def test_actualiza_idioma(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma/' + str(id_idioma), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 200
    assert resp.json.get('name') == 'Prueba Nombre 1'
    assert resp.json.get('description') == 'Prueba Description 1'
 
def test_actualiza_idioma_id_no_numeric(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + 'dddd' + '/idioma/' + str(id_idioma), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma/' + '5ddd', json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/dddd/perfil/' + str(id_perfil) + '/idioma/' + str(id_idioma), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400


def test_actualiza_idioma_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/idioma/' + str(id_idioma), json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 404
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma/' + '1234', json={'name': "Prueba Nombre 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 404

def test_actualiza_idioma_datos_incompletos(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma/' + str(id_idioma), json={'name': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma/' + str(id_idioma), json={'description': ''})
    assert resp.status_code == 400


def test_obtiene_idioma(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma')
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['name'] == 'Prueba Nombre 1'


def test_obtiene_idioma_perfil_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '123' + '/idioma')
    assert resp.status_code == 404

    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/1234/perfil/' + str(id_perfil) + '/idioma')
    assert resp.status_code == 404

def test_obtiene_idioma_id(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma/' + str(id_idioma))
    assert resp.status_code == 200
    assert resp.json.get('name') == 'Prueba Nombre 1'

def test_obtiene_idioma_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/idioma/' + str(id_idioma))
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma/' + '1234')
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + '1234' + '/perfil/' + str(id_perfil) + '/idioma/' + str(id_idioma))
    assert resp.status_code == 404

def test_elimina_idioma(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma/' + str(id_idioma))
    assert resp.status_code == 204

def test_elimina_idioma_id_no_existe(client: FlaskClient):
    global id_perfil, id_empresa, id_proyecto, id_idioma
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + '1234' + '/idioma/' + str(id_idioma))
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto) + '/perfil/' + str(id_perfil) + '/idioma/' + '1234')
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/44444/perfil/' + str(id_perfil) + '/idioma/' + str(id_idioma))
    assert resp.status_code == 404


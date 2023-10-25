import pytest
from flask.testing import FlaskClient
from src.app import app, db
from src.modelos import Candidato, InformacionAcademica, InformacionTecnica, InformacionLaboral
import requests
import os

id_candidato = 0
id_informacion_tecnica = 0
id_informacion_academica = 0
id_informacion_laboral = 0

@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    InformacionAcademica.query.delete()
    InformacionTecnica.query.delete()
    InformacionLaboral.query.delete()
    Candidato.query.delete()

@pytest.fixture
def client():
    #Usuario.query.delete()
    #db.session.commit()
    return app.test_client()

# Pruebas candidatos
def test_registro_candidato(client: FlaskClient):
    resp = client.post(
        '/candidato', json={'names': 'César Hernán','lastNames': 'García Afanador','mail': 'cesa96@gmail.com','password': 'prueba1','confirmPassword': 'prueba1'})
    assert resp.status_code == 201
    assert resp.json.get('id')    
    global id_candidato
    id_candidato = resp.json.get('id')


def test_registro_candidato_password_incorrecto(client: FlaskClient):
    resp = client.post(
        '/candidato', json={'names': 'César Hernán','lastNames': 'García Afanador','mail': 'cesa96@gmail.com','password': 'prueba1','confirmPassword': 'prueba2'})
    assert resp.status_code == 409  

def test_registro_candidato_datos_incompletos(client: FlaskClient):
    resp = client.post(
        '/candidato', json={'names': 'César Hernán','lastNames': 'García Afanador','password': 'prueba1','confirmPassword': 'prueba1'})
    assert resp.status_code == 400  
    resp = client.post(
        '/candidato', json={'names': 'César Hernán','lastNames': 'García Afanador','mail': '','password': 'prueba1','confirmPassword': 'prueba1'})
    assert resp.status_code == 400  

def test_actualiza_candidato(client: FlaskClient):
    global id_candidato
    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'names': 'César',
                                            'lastNames': 'García',
                                            'mail': 'cesa96@hotmail.com',
                                            'docType': 'CC',
                                            'docNumber': '13514130',
                                            'phone': '3102062948',
                                            'address': 'Cll 10 a sur # 2a - 128',
                                            'birthDate': '1978-03-15T00:00:00.000Z',
                                            'country': 'Colombia',
                                            'city': 'Cajicá',
                                            'language': 'Español'})
    assert resp.status_code == 200
    assert resp.json.get('names') == 'César'
    assert resp.json.get('lastNames') == 'García'
    assert resp.json.get('mail') == 'cesa96@hotmail.com'
    assert resp.json.get('docType') == 'CC'
    assert resp.json.get('docNumber') == '13514130'
    assert resp.json.get('address') == 'Cll 10 a sur # 2a - 128'
    assert resp.json.get('country') == 'Colombia'
    assert resp.json.get('city') == 'Cajicá'
    assert resp.json.get('language') == 'Español'

def test_actualiza_candidato_id_no_numeric(client: FlaskClient):
    global id_candidato

    resp = client.patch(
        '/candidato/lll', json={'names': 'César',
                                            'lastNames': 'García',
                                            'mail': 'cesa96@hotmail.com',
                                            'docType': 'CC',
                                            'docNumber': '13514130',
                                            'phone': '3102062948',
                                            'address': 'Cll 10 a sur # 2a - 128',
                                            'birthDate': '1978-03-15T00:00:00.000Z',
                                            'country': 'Colombia',
                                            'city': 'Cajicá',
                                            'language': 'Español'})
    assert resp.status_code == 400


def test_actualiza_candidato_datos_incompletos(client: FlaskClient):
    global id_candidato

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'names': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'lastNames': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'mail': '',})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'docType': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'docNumber': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'phone': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'address': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'birthDate': '1978-15-15T00:00:00.000Z'})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'country': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'city': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato), json={'language': ''})
    assert resp.status_code == 400

def test_obtiene_candidatos(client: FlaskClient):
    resp = client.get(
        '/candidato')
    assert resp.status_code == 200
    jsonreponse = resp.json
    #assert jsonreponse[0]['Names'] == 'César'

def test_obtiene_candidatos_x_mail(client: FlaskClient):
    resp = client.get(
        "/candidato?mail=cesa96@hotmail.com")
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['names'] == 'César'

def test_obtiene_candidatos_id(client: FlaskClient):
    global id_candidato
    resp = client.get(
        "/candidato/" + str(id_candidato))
    assert resp.status_code == 200
    assert resp.json.get('names') == 'César'

# Pruebas Información Académica

def test_crea_informacion_academica(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.post(
        '/candidato/' + str(id_candidato) + '/informacionAcademica', json={'title': "Prueba Titulo",'institution': 'Prueba Institution','beginDate': '2008-03-15T00:00:00.000Z','endDate': '2010-03-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_informacion_academica = resp.json.get('id')

def test_crea_informacion_academica_datos_incompletos(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.post(
        '/candidato/' + str(id_candidato) + '/informacionAcademica', json={'title': "Prueba Titulo",'beginDate': '2008-03-15T00:00:00.000Z','endDate': '2010-03-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
    assert resp.status_code == 400
    resp = client.post(
        '/candidato/' + str(id_candidato) + '/informacionAcademica', json={'title': "Prueba Titulo",'institution': 'Prueba Institution','beginDate': '2008-15-15T00:00:00.000Z','endDate': '2010-03-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
    assert resp.status_code == 400
    resp = client.post(
        '/candidato/' + str(id_candidato) + '/informacionAcademica', json={'title': "Prueba Titulo",'institution': 'Prueba Institution','beginDate': '2008-03-15T00:00:00.000Z','endDate': '2010-15-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
    assert resp.status_code == 400

def test_crea_informacion_academica_candidato_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.post(
        '/candidato/123456/informacionAcademica', json={'title': "Prueba Titulo",'institution': 'Prueba Institution','beginDate': '2008-03-15T00:00:00.000Z','endDate': '2010-03-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
    assert resp.status_code == 404
    resp = client.post(
        '/candidato/dd444/informacionAcademica', json={'title': "Prueba Titulo",'institution': 'Prueba Institution','beginDate': '2008-03-15T00:00:00.000Z','endDate': '2010-03-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
    assert resp.status_code == 400

def test_actualiza_informacion_academica(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + str(id_informacion_academica), json={'title': "Prueba Titulo 1",'institution': 'Prueba Institution 1','beginDate': '2008-04-15T00:00:00.000Z','endDate': None,'studyType': 'Prueba Tipo 2'})
    assert resp.status_code == 200
    assert resp.json.get('title') == 'Prueba Titulo 1'
    assert resp.json.get('institution') == 'Prueba Institution 1'
    assert resp.json.get('studyType') == 'Prueba Tipo 2'



def test_actualiza_informacion_academica_id_no_numeric(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.patch(
        '/candidato/' + 'dddd' + '/informacionAcademica/' + str(id_informacion_academica), json={'title': "Prueba Titulo 1",'institution': 'Prueba Institution 1','beginDate': '2008-04-15T00:00:00.000Z','endDate': None,'studyType': 'Prueba Tipo 2'})
    assert resp.status_code == 400
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + '5ddd', json={'title': "Prueba Titulo 1",'institution': 'Prueba Institution 1','beginDate': '2008-04-15T00:00:00.000Z','endDate': None,'studyType': 'Prueba Tipo 2'})
    assert resp.status_code == 400


def test_actualiza_informacion_academica_id_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.patch(
        '/candidato/' + '1234' + '/informacionAcademica/' + str(id_informacion_academica), json={'title': "Prueba Titulo 1",'institution': 'Prueba Institution 1','beginDate': '2008-04-15T00:00:00.000Z','endDate': None,'studyType': 'Prueba Tipo 2'})
    assert resp.status_code == 404
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + '1234', json={'title': "Prueba Titulo 1",'institution': 'Prueba Institution 1','beginDate': '2008-04-15T00:00:00.000Z','endDate': None,'studyType': 'Prueba Tipo 2'})
    assert resp.status_code == 404

def test_actualiza_informacion_academica_datos_incompletos(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + str(id_informacion_academica), json={'title': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + str(id_informacion_academica), json={'institution': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + str(id_informacion_academica), json={'beginDate': None})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + str(id_informacion_academica), json={'studyType': ''})
    assert resp.status_code == 400


def test_obtiene_informacion_academica(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/informacionAcademica')
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['title'] == 'Prueba Titulo 1'


def test_obtiene_informacion_academica_candidato_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.get(
        '/candidato/' + '123' + '/informacionAcademica')
    assert resp.status_code == 404

def test_obtiene_informacion_academica_id(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + str(id_informacion_academica))
    assert resp.status_code == 200
    assert resp.json.get('title') == 'Prueba Titulo 1'

def test_obtiene_informacion_academica_id_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.get(
        '/candidato/' + '1234' + '/informacionAcademica/' + str(id_informacion_academica))
    assert resp.status_code == 404
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + '1234')
    assert resp.status_code == 404


def test_elimina_informacion_academica(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.delete(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + str(id_informacion_academica))
    assert resp.status_code == 204

def test_elimina_informacion_academica_id_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_academica
    resp = client.delete(
        '/candidato/' + '1234' + '/informacionAcademica/' + str(id_informacion_academica))
    assert resp.status_code == 404
    resp = client.delete(
        '/candidato/' + str(id_candidato) + '/informacionAcademica/' + '1234')
    assert resp.status_code == 404


# Pruebas Información Técnica

def test_crea_informacion_tecnica(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.post(
        '/candidato/' + str(id_candidato) + '/informacionTecnica', json={'type': "Prueba Tipo",'description': 'Prueba Descripcion'})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_informacion_tecnica = resp.json.get('id')

def test_crea_informacion_tecnica_datos_incompletos(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.post(
        '/candidato/' + str(id_candidato) + '/informacionTecnica', json={'type': "Prueba Tipo"})
    assert resp.status_code == 400
    resp = client.post(
        '/candidato/' + str(id_candidato) + '/informacionTecnica', json={'type': "Prueba Tipo",'description': ''})
    assert resp.status_code == 400

def test_crea_informacion_tecnica_candidato_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.post(
        '/candidato/123456/informacionTecnica', json={'type': "Prueba Tipo",'description': 'Prueba Descripcion'})
    assert resp.status_code == 404
    resp = client.post(
        '/candidato/ddddd/informacionTecnica', json={'type': "Prueba Tipo",'description': 'Prueba Descripcion'})
    assert resp.status_code == 400

def test_actualiza_informacion_tecnica(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionTecnica/' + str(id_informacion_tecnica), json={'type': "Prueba Tipo 1",'description': 'Prueba Descripcion 1'})
    assert resp.status_code == 200
    assert resp.json.get('type') == 'Prueba Tipo 1'
    assert resp.json.get('description') == 'Prueba Descripcion 1'



def test_actualiza_informacion_tecnica_id_no_numeric(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.patch(
        '/candidato/' + 'dddd' + '/informacionTecnica/' + str(id_informacion_tecnica), json={'type': "Prueba Tipo 1",'description': 'Prueba Descripcion 1'})
    assert resp.status_code == 400
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionTecnica/' + '5ddd', json={'type': "Prueba Tipo 1",'description': 'Prueba Descripcion 1'})
    assert resp.status_code == 400


def test_actualiza_informacion_tecnica_id_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.patch(
        '/candidato/' + '1234' + '/informacionTecnica/' + str(id_informacion_tecnica), json={'type': "Prueba Tipo 1",'description': 'Prueba Descripcion 1'})
    assert resp.status_code == 404
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionTecnica/' + '1234', json={'type': "Prueba Tipo 1",'description': 'Prueba Descripcion 1'})
    assert resp.status_code == 404

def test_actualiza_informacion_tecnica_datos_incompletos(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionTecnica/' + str(id_informacion_tecnica), json={'type': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionTecnica/' + str(id_informacion_tecnica), json={'description': ''})
    assert resp.status_code == 400


def test_obtiene_informacion_tecnica(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/informacionTecnica')
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['type'] == 'Prueba Tipo 1'


def test_obtiene_informacion_tecnica_candidato_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.get(
        '/candidato/' + '123' + '/informacionTecnica')
    assert resp.status_code == 404

def test_obtiene_informacion_tecnica_id(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/informacionTecnica/' + str(id_informacion_tecnica))
    assert resp.status_code == 200
    assert resp.json.get('type') == 'Prueba Tipo 1'

def test_obtiene_informacion_tecnica_id_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.get(
        '/candidato/' + '1234' + '/informacionTecnica/' + str(id_informacion_tecnica))
    assert resp.status_code == 404
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/informacionTecnica/' + '1234')
    assert resp.status_code == 404


def test_elimina_informacion_tecnica(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.delete(
        '/candidato/' + str(id_candidato) + '/informacionTecnica/' + str(id_informacion_tecnica))
    assert resp.status_code == 204

def test_elimina_informacion_tecnica_id_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_tecnica
    resp = client.delete(
        '/candidato/' + '1234' + '/informacionTecnica/' + str(id_informacion_tecnica))
    assert resp.status_code == 404
    resp = client.delete(
        '/candidato/' + str(id_candidato) + '/informacionTecnica/' + '1234')
    assert resp.status_code == 404


# Pruebas Información Laboral

def test_crea_informacion_laboral(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.post(
        '/candidato/' + str(id_candidato) + '/informacionLaboral', json={'position': "Prueba Cargo",'organization': 'Prueba empresa', 'activities': 'Estas son algunas actividades', 'dateFrom': '2003-03-15T00:00:00.000Z', 'dateTo' : '2005-03-15T00:00:00.000Z'})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_informacion_laboral = resp.json.get('id')

def test_crea_informacion_laboral_datos_incompletos(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.post(
        '/candidato/' + str(id_candidato) + '/informacionLaboral', json={'position': "Prueba Cargo",'organization': 'Prueba empresa', 'dateFrom': '2003-03-15T00:00:00.000Z'})
    assert resp.status_code == 400
    resp = client.post(
        '/candidato/' + str(id_candidato) + '/informacionLaboral', json={'position': "Prueba Cargo",'organization': '', 'activities': 'Estas son algunas actividades', 'dateFrom': '2003-03-15T00:00:00.000Z'})
    assert resp.status_code == 400

def test_crea_informacion_laboral_candidato_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.post(
        '/candidato/123456/informacionLaboral', json={'position': "Prueba Cargo",'organization': 'Prueba empresa', 'activities': 'Estas son algunas actividades', 'dateFrom': '2003-03-15T00:00:00.000Z'})
    assert resp.status_code == 404
    resp = client.post(
        '/candidato/ddddd/informacionLaboral', json={'position': "Prueba Cargo",'organization': 'Prueba empresa', 'activities': 'Estas son algunas actividades', 'dateFrom': '2003-03-15T00:00:00.000Z'})
    assert resp.status_code == 400

def test_actualiza_informacion_laboral(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + str(id_informacion_laboral), json={'position': 'Prueba Cargo 2','organization': 'Prueba empresa 2', 'activities': 'Estas son algunas actividades 2', 'dateFrom': '2004-03-15T00:00:00.000Z', 'dateTo' : None})
    assert resp.status_code == 200
    assert resp.json.get('position') == 'Prueba Cargo 2'
    assert resp.json.get('organization') == 'Prueba empresa 2'
    assert resp.json.get('activities') == 'Estas son algunas actividades 2'



def test_actualiza_informacion_laboral_id_no_numeric(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.patch(
        '/candidato/' + 'dddd' + '/informacionLaboral/' + str(id_informacion_laboral), json={'position': 'Prueba Cargo 2','organization': 'Prueba empresa 2', 'activities': 'Estas son algunas actividades 2', 'dateFrom': '2004-03-15T00:00:00.000Z', 'dateTo' : None})
    assert resp.status_code == 400
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + '5ddd', json={'position': 'Prueba Cargo 2','organization': 'Prueba empresa 2', 'activities': 'Estas son algunas actividades 2', 'dateFrom': '2004-03-15T00:00:00.000Z', 'dateTo' : None})
    assert resp.status_code == 400


def test_actualiza_informacion_laboral_id_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.patch(
        '/candidato/' + '1234' + '/informacionLaboral/' + str(id_informacion_laboral), json={'position': 'Prueba Cargo 2','organization': 'Prueba empresa 2', 'activities': 'Estas son algunas actividades 2', 'dateFrom': '2004-03-15T00:00:00.000Z', 'dateTo' : None})
    assert resp.status_code == 404
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + '1234', json={'position': 'Prueba Cargo 2','organization': 'Prueba empresa 2', 'activities': 'Estas son algunas actividades 2', 'dateFrom': '2004-03-15T00:00:00.000Z', 'dateTo' : None})
    assert resp.status_code == 404

def test_actualiza_informacion_laboral_datos_incompletos(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + str(id_informacion_laboral), json={'position': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + str(id_informacion_laboral), json={'organization': ''})
    assert resp.status_code == 400
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + str(id_informacion_laboral), json={'activities': ''})
    assert resp.status_code == 400
    resp = client.patch(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + str(id_informacion_laboral), json={'dateFrom': ''})
    assert resp.status_code == 400


def test_obtiene_informacion_laboral(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/informacionLaboral')
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['position'] == 'Prueba Cargo 2'


def test_obtiene_informacion_laboral_candidato_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.get(
        '/candidato/' + '123' + '/informacionLaboral')
    assert resp.status_code == 404

def test_obtiene_informacion_laboral_id(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + str(id_informacion_laboral))
    assert resp.status_code == 200
    assert resp.json.get('position') == 'Prueba Cargo 2'

def test_obtiene_informacion_laboral_id_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.get(
        '/candidato/' + '1234' + '/informacionLaboral/' + str(id_informacion_laboral))
    assert resp.status_code == 404
    resp = client.get(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + '1234')
    assert resp.status_code == 404


def test_elimina_informacion_laboral(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.delete(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + str(id_informacion_laboral))
    assert resp.status_code == 204

def test_elimina_informacion_laboral_id_no_existe(client: FlaskClient):
    global id_candidato, id_informacion_laboral
    resp = client.delete(
        '/candidato/' + '1234' + '/informacionLaboral/' + str(id_informacion_laboral))
    assert resp.status_code == 404
    resp = client.delete(
        '/candidato/' + str(id_candidato) + '/informacionLaboral/' + '1234')
    assert resp.status_code == 404
    
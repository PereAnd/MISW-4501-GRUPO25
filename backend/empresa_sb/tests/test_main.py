import pytest
from flask.testing import FlaskClient
from src.app import app
import requests
import os
import time

id_empresa = 0
id_vertical = 0
id_ubicacion = 0

@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    pass
    # InformacionAcademica.query.delete()
    # InformacionTecnica.query.delete()
    # InformacionLaboral.query.delete()
    # Empresa.query.delete()

@pytest.fixture
def client():
    #Usuario.query.delete()
    #db.session.commit()
    return app.test_client()

# Pruebas empresas
def test_registro_empresa(client: FlaskClient):
    resp = client.post(
        '/empresa', json={'name': 'CIRKUS SAS','mail': 'cesa96@gmail.com','password': 'prueba1','confirmPassword': 'prueba1'})
    assert resp.status_code == 201
    assert resp.json.get('id')    
    global id_empresa
    id_empresa = resp.json.get('id')


def test_registro_empresa_password_incorrecto(client: FlaskClient):
    resp = client.post(
        '/empresa', json={'name': 'CIRKUS SAS','mail': 'cesa96@gmail.com','password': 'prueba1','confirmPassword': 'prueba2'})
    assert resp.status_code == 409  

def test_registro_empresa_datos_incompletos(client: FlaskClient):
    resp = client.post(
        '/empresa', json={'name': 'CIRKUS SAS','password': 'prueba1','confirmPassword': 'prueba1'})
    assert resp.status_code == 400  
    resp = client.post(
        '/empresa', json={'name': 'CIRKUS SAS','mail': '','password': 'prueba1','confirmPassword': 'prueba1'})
    assert resp.status_code == 400  


def test_actualiza_empresa(client: FlaskClient):
    global id_empresa
    resp = client.patch(
        '/empresa/' + str(id_empresa), json={'name': 'Otra Empresa',
                                            'mail': 'cesa96@hotmail.com',
                                            'docType': 'NIT',
                                            'docNumber': '900874520',
                                            'organizationType': 'SAS',
                                            'description': 'esta es una prueba de la descripción'})
    assert resp.status_code == 200
    assert resp.json.get('name') == 'Otra Empresa'
    assert resp.json.get('mail') == 'cesa96@hotmail.com'
    assert resp.json.get('docType') == 'NIT'
    assert resp.json.get('docNumber') == '900874520'
    assert resp.json.get('organizationType') == 'SAS'
    assert resp.json.get('description') == 'esta es una prueba de la descripción'

def test_actualiza_empresa_id_no_numeric(client: FlaskClient):
    global id_empresa

    resp = client.patch(
        '/empresa/lll', json={'name': 'Otra Empresa',
                                            'mail': 'cesa96@hotmail.com',
                                            'docType': 'NIT',
                                            'docNumber': '900874520',
                                            'organizationType': 'SAS',
                                            'description': 'esta es una prueba de la descripción'})
    assert resp.status_code == 400


def test_actualiza_empresa_datos_incompletos(client: FlaskClient):
    global id_empresa

    resp = client.patch(
        '/empresa/' + str(id_empresa), json={'name': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa), json={'mail': '',})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa), json={'docType': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa), json={'docNumber': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa), json={'organizationType': ''})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa), json={'description': ''})
    assert resp.status_code == 400

def test_obtiene_empresas(client: FlaskClient):
    resp = client.get(
        '/empresa')
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['name'] == 'Otra Empresa'

def test_obtiene_empresas_x_mail(client: FlaskClient):
    resp = client.get(
        "/empresa?mail=cesa96@hotmail.com")
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['name'] == 'Otra Empresa'

def test_obtiene_empresas_id(client: FlaskClient):
    global id_empresa
    resp = client.get(
        "/empresa/" + str(id_empresa))
    assert resp.status_code == 200
    assert resp.json.get('name') == 'Otra Empresa'



# Pruebas Vertical

def test_crea_vertical(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/vertical', json={'vertical': "Prueba Vertical",'description': 'Prueba Description'})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_vertical = resp.json.get('id')

def test_crea_vertical_datos_incompletos(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/vertical', json={'vertical': "Prueba Vertical"})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/vertical', json={'vertical': "Prueba Vertical",'description': ''})
    assert resp.status_code == 400

def test_crea_vertical_empresa_no_existe(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.post(
        '/empresa/123456/vertical', json={'vertical': "Prueba Vertical",'description': 'Prueba Description'})
    assert resp.status_code == 404

def test_actualiza_vertical(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/vertical/' + str(id_vertical), json={'vertical': "Prueba Vertical 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 200
    assert resp.json.get('vertical') == 'Prueba Vertical 1'
    assert resp.json.get('description') == 'Prueba Description 1'

def test_actualiza_vertical_id_no_numeric(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.patch(
        '/empresa/' + 'dddd' + '/vertical/' + str(id_vertical), json={'vertical': "Prueba Vertical 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/vertical/' + '5ddd', json={'vertical': "Prueba Vertical 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400


def test_actualiza_vertical_id_no_existe(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.patch(
        '/empresa/' + '1234' + '/vertical/' + str(id_vertical), json={'vertical': "Prueba Vertical 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 404
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/vertical/' + '1234', json={'vertical': "Prueba Vertical 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 404

def test_actualiza_vertical_datos_incompletos(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/vertical/' + str(id_vertical), json={'vertical': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/vertical/' + str(id_vertical), json={'description': ''})
    assert resp.status_code == 400

def test_obtiene_vertical(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/vertical')
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['vertical'] == 'Prueba Vertical 1'
    # assert jsonreponse == 'Prueba Vertical 1'


def test_obtiene_vertical_empresa_no_existe(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.get(
        '/empresa/' + '123' + '/vertical')
    assert resp.status_code == 404

def test_obtiene_vertical_id(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/vertical/' + str(id_vertical))
    assert resp.status_code == 200
    assert resp.json.get('vertical') == 'Prueba Vertical 1'

def test_obtiene_vertical_id_no_existe(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.get(
        '/empresa/' + '1234' + '/vertical/' + str(id_vertical))
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/vertical/' + '1234')
    assert resp.status_code == 404


def test_elimina_vertical(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/vertical/' + str(id_vertical))
    assert resp.status_code == 204

def test_elimina_vertical_id_no_existe(client: FlaskClient):
    global id_empresa, id_vertical
    resp = client.delete(
        '/empresa/' + '1234' + '/vertical/' + str(id_vertical))
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/vertical/' + '1234')
    assert resp.status_code == 404



# Pruebas Ubicación

def test_crea_ubicacion(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/ubicacion', json={'country': "Prueba País",'city': "Prueba City",'description': 'Prueba Description'})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_ubicacion = resp.json.get('id')

def test_crea_ubicacion_datos_incompletos(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/ubicacion', json={'country': "Prueba País",'description': 'Prueba Description'})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/ubicacion', json={'country': "Prueba País",'city': "",'description': 'Prueba Description'})
    assert resp.status_code == 400

def test_crea_ubicacion_empresa_no_existe(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.post(
        '/empresa/123456/ubicacion', json={'country': "Prueba País",'city': "Prueba City",'description': 'Prueba Description'})
    assert resp.status_code == 404

def test_actualiza_ubicacion(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/ubicacion/' + str(id_ubicacion), json={'country': "Prueba País 1",'city': "Prueba City 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 200
    assert resp.json.get('country') == 'Prueba País 1'
    assert resp.json.get('city') == 'Prueba City 1'
    assert resp.json.get('description') == 'Prueba Description 1'

def test_actualiza_ubicacion_id_no_numeric(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.patch(
        '/empresa/' + 'dddd' + '/ubicacion/' + str(id_ubicacion), json={'country': "Prueba País",'city': "Prueba City",'description': 'Prueba Description'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/ubicacion/' + '5ddd', json={'country': "Prueba País",'city': "Prueba City",'description': 'Prueba Description'})
    assert resp.status_code == 400


def test_actualiza_ubicacion_id_no_existe(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.patch(
        '/empresa/' + '1234' + '/ubicacion/' + str(id_ubicacion), json={'country': "Prueba País",'city': "Prueba City",'description': 'Prueba Description'})
    assert resp.status_code == 404
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/ubicacion/' + '1234', json={'country': "Prueba País",'city': "Prueba City",'description': 'Prueba Description'})
    assert resp.status_code == 404

def test_actualiza_ubicacion_datos_incompletos(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/ubicacion/' + str(id_ubicacion), json={'country': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/ubicacion/' + str(id_ubicacion), json={'city': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/ubicacion/' + str(id_ubicacion), json={'description': ''})
    assert resp.status_code == 400

def test_obtiene_ubicacion(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/ubicacion')
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['country'] == 'Prueba País 1'
    # assert jsonreponse == 'Prueba Ubicacion 1'


def test_obtiene_ubicacion_empresa_no_existe(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.get(
        '/empresa/' + '123' + '/ubicacion')
    assert resp.status_code == 404

def test_obtiene_ubicacion_id(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/ubicacion/' + str(id_ubicacion))
    assert resp.status_code == 200
    assert resp.json.get('country') == 'Prueba País 1'

def test_obtiene_ubicacion_id_no_existe(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.get(
        '/empresa/' + '1234' + '/ubicacion/' + str(id_ubicacion))
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/ubicacion/' + '1234')
    assert resp.status_code == 404


def test_elimina_ubicacion(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/ubicacion/' + str(id_ubicacion))
    assert resp.status_code == 204

def test_elimina_ubicacion_id_no_existe(client: FlaskClient):
    global id_empresa, id_ubicacion
    resp = client.delete(
        '/empresa/' + '1234' + '/ubicacion/' + str(id_ubicacion))
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/ubicacion/' + '1234')
    assert resp.status_code == 404

# Pruebas Proyecto

def test_crea_proyecto(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto', json={'proyecto': "Prueba Proyecto",'description': 'Prueba Description'})
    assert resp.status_code == 201
    assert resp.json.get('id')
    id_proyecto = resp.json.get('id')

def test_crea_proyecto_datos_incompletos(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto', json={'proyecto': "Prueba Proyecto"})
    assert resp.status_code == 400
    resp = client.post(
        '/empresa/' + str(id_empresa) + '/proyecto', json={'proyecto': "Prueba Proyecto",'description': ''})
    assert resp.status_code == 400

def test_crea_proyecto_empresa_no_existe(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.post(
        '/empresa/123456/proyecto', json={'proyecto': "Prueba Proyecto",'description': 'Prueba Description'})
    assert resp.status_code == 404

def test_actualiza_proyecto(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto), json={'proyecto': "Prueba Proyecto 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 200
    assert resp.json.get('proyecto') == 'Prueba Proyecto 1'
    assert resp.json.get('description') == 'Prueba Description 1'

def test_actualiza_proyecto_id_no_numeric(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.patch(
        '/empresa/' + 'dddd' + '/proyecto/' + str(id_proyecto), json={'proyecto': "Prueba Proyecto 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + '5ddd', json={'proyecto': "Prueba Proyecto 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 400


def test_actualiza_proyecto_id_no_existe(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.patch(
        '/empresa/' + '1234' + '/proyecto/' + str(id_proyecto), json={'proyecto': "Prueba Proyecto 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 404
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + '1234', json={'proyecto': "Prueba Proyecto 1",'description': 'Prueba Description 1'})
    assert resp.status_code == 404

def test_actualiza_proyecto_datos_incompletos(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto), json={'proyecto': ""})
    assert resp.status_code == 400

    resp = client.patch(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto), json={'description': ''})
    assert resp.status_code == 400

def test_obtiene_proyecto(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto')
    assert resp.status_code == 200
    jsonreponse = resp.json
    assert jsonreponse[0]['proyecto'] == 'Prueba Proyecto 1'
    # assert jsonreponse == 'Prueba Proyecto 1'


def test_obtiene_proyecto_empresa_no_existe(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.get(
        '/empresa/' + '123' + '/proyecto')
    assert resp.status_code == 404

def test_obtiene_proyecto_id(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto))
    assert resp.status_code == 200
    assert resp.json.get('proyecto') == 'Prueba Proyecto 1'

def test_obtiene_proyecto_id_no_existe(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.get(
        '/empresa/' + '1234' + '/proyecto/' + str(id_proyecto))
    assert resp.status_code == 404
    resp = client.get(
        '/empresa/' + str(id_empresa) + '/proyecto/' + '1234')
    assert resp.status_code == 404


def test_elimina_proyecto(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + str(id_proyecto))
    assert resp.status_code == 204

def test_elimina_proyecto_id_no_existe(client: FlaskClient):
    global id_empresa, id_proyecto
    resp = client.delete(
        '/empresa/' + '1234' + '/proyecto/' + str(id_proyecto))
    assert resp.status_code == 404
    resp = client.delete(
        '/empresa/' + str(id_empresa) + '/proyecto/' + '1234')
    assert resp.status_code == 404










def test_circuit_breaker(client: FlaskClient):
    global id_empresa, id_informacion_tecnica
    tempEnv = os.environ["EMPR_BACK_URL"]
    os.environ["EMPR_BACK_URL"] = 'http://noexiste.com:5001'
    resp = client.get(
        "/empresa?mail=cesa96@hotmail.com") 
    assert resp.status_code == 503
    resp = client.get(
        "/empresa?mail=cesa96@hotmail.com")
    assert resp.status_code == 503
    resp = client.get(
        "/empresa?mail=cesa96@hotmail.com")
    assert resp.status_code == 503
    resp = client.get(
        "/empresa?mail=cesa96@hotmail.com")
    assert resp.status_code == 503
    resp = client.get(
        "/empresa?mail=cesa96@hotmail.com")
    assert resp.status_code == 503
    resp = client.get(
        "/empresa?mail=cesa96@hotmail.com")
    assert resp.status_code == 503
    os.environ["EMPR_BACK_URL"] = tempEnv   
    resp = client.get(
        "/empresa?mail=cesa96@hotmail.com")
    assert resp.status_code == 503

    time.sleep(10)
    resp = client.get(
        "/empresa?mail=cesa96@hotmail.com")
    assert resp.status_code == 200

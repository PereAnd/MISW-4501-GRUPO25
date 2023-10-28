import pytest
from flask.testing import FlaskClient
from src.app import app, db
from src.modelos import Empresa #, InformacionAcademica, InformacionTecnica, InformacionLaboral
import requests
import os

id_empresa = 0
id_informacion_tecnica = 0
id_informacion_academica = 0
id_informacion_laboral = 0

@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    # InformacionAcademica.query.delete()
    # InformacionTecnica.query.delete()
    # InformacionLaboral.query.delete()
    Empresa.query.delete()

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

# def test_actualiza_empresa(client: FlaskClient):
#     global id_empresa
#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'names': 'César',
#                                             'lastNames': 'García',
#                                             'mail': 'cesa96@hotmail.com',
#                                             'docType': 'CC',
#                                             'docNumber': '13514130',
#                                             'phone': '3102062948',
#                                             'address': 'Cll 10 a sur # 2a - 128',
#                                             'birthDate': '1978-03-15T00:00:00.000Z',
#                                             'country': 'Colombia',
#                                             'city': 'Cajicá',
#                                             'language': 'Español'})
#     assert resp.status_code == 200
#     assert resp.json.get('names') == 'César'
#     assert resp.json.get('lastNames') == 'García'
#     assert resp.json.get('mail') == 'cesa96@hotmail.com'
#     assert resp.json.get('docType') == 'CC'
#     assert resp.json.get('docNumber') == '13514130'
#     assert resp.json.get('address') == 'Cll 10 a sur # 2a - 128'
#     assert resp.json.get('country') == 'Colombia'
#     assert resp.json.get('city') == 'Cajicá'
#     assert resp.json.get('language') == 'Español'

# def test_actualiza_empresa_id_no_numeric(client: FlaskClient):
#     global id_empresa

#     resp = client.patch(
#         '/empresa/lll', json={'names': 'César',
#                                             'lastNames': 'García',
#                                             'mail': 'cesa96@hotmail.com',
#                                             'docType': 'CC',
#                                             'docNumber': '13514130',
#                                             'phone': '3102062948',
#                                             'address': 'Cll 10 a sur # 2a - 128',
#                                             'birthDate': '1978-03-15T00:00:00.000Z',
#                                             'country': 'Colombia',
#                                             'city': 'Cajicá',
#                                             'language': 'Español'})
#     assert resp.status_code == 400


# def test_actualiza_empresa_datos_incompletos(client: FlaskClient):
#     global id_empresa

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'names': ''})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'lastNames': ''})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'mail': '',})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'docType': ''})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'docNumber': ''})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'phone': ''})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'address': ''})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'birthDate': '1978-15-15T00:00:00.000Z'})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'country': ''})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'city': ''})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa), json={'language': ''})
#     assert resp.status_code == 400

# def test_obtiene_empresas(client: FlaskClient):
#     resp = client.get(
#         '/empresa')
#     assert resp.status_code == 200
#     jsonreponse = resp.json
#     #assert jsonreponse[0]['Names'] == 'César'

# def test_obtiene_empresas_x_mail(client: FlaskClient):
#     resp = client.get(
#         "/empresa?mail=cesa96@hotmail.com")
#     assert resp.status_code == 200
#     jsonreponse = resp.json
#     assert jsonreponse[0]['names'] == 'César'

# def test_obtiene_empresas_id(client: FlaskClient):
#     global id_empresa
#     resp = client.get(
#         "/empresa/" + str(id_empresa))
#     assert resp.status_code == 200
#     assert resp.json.get('names') == 'César'

# # Pruebas Información Académica

# def test_crea_informacion_academica(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.post(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica', json={'title': "Prueba Titulo",'institution': 'Prueba Institution','beginDate': '2008-03-15T00:00:00.000Z','endDate': '2010-03-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
#     assert resp.status_code == 201
#     assert resp.json.get('id')
#     id_informacion_academica = resp.json.get('id')

# def test_crea_informacion_academica_datos_incompletos(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.post(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica', json={'title': "Prueba Titulo",'beginDate': '2008-03-15T00:00:00.000Z','endDate': '2010-03-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
#     assert resp.status_code == 400
#     resp = client.post(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica', json={'title': "Prueba Titulo",'institution': 'Prueba Institution','beginDate': '2008-15-15T00:00:00.000Z','endDate': '2010-03-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
#     assert resp.status_code == 400
#     resp = client.post(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica', json={'title': "Prueba Titulo",'institution': 'Prueba Institution','beginDate': '2008-03-15T00:00:00.000Z','endDate': '2010-15-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
#     assert resp.status_code == 400

# def test_crea_informacion_academica_empresa_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.post(
#         '/empresa/123456/informacionAcademica', json={'title': "Prueba Titulo",'institution': 'Prueba Institution','beginDate': '2008-03-15T00:00:00.000Z','endDate': '2010-03-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
#     assert resp.status_code == 404
#     resp = client.post(
#         '/empresa/dd444/informacionAcademica', json={'title': "Prueba Titulo",'institution': 'Prueba Institution','beginDate': '2008-03-15T00:00:00.000Z','endDate': '2010-03-15T00:00:00.000Z','studyType': 'Prueba Tipo'})
#     assert resp.status_code == 400

# def test_actualiza_informacion_academica(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + str(id_informacion_academica), json={'title': "Prueba Titulo 1",'institution': 'Prueba Institution 1','beginDate': '2008-04-15T00:00:00.000Z','endDate': None,'studyType': 'Prueba Tipo 2'})
#     assert resp.status_code == 200
#     assert resp.json.get('title') == 'Prueba Titulo 1'
#     assert resp.json.get('institution') == 'Prueba Institution 1'
#     assert resp.json.get('studyType') == 'Prueba Tipo 2'



# def test_actualiza_informacion_academica_id_no_numeric(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.patch(
#         '/empresa/' + 'dddd' + '/informacionAcademica/' + str(id_informacion_academica), json={'title': "Prueba Titulo 1",'institution': 'Prueba Institution 1','beginDate': '2008-04-15T00:00:00.000Z','endDate': None,'studyType': 'Prueba Tipo 2'})
#     assert resp.status_code == 400
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + '5ddd', json={'title': "Prueba Titulo 1",'institution': 'Prueba Institution 1','beginDate': '2008-04-15T00:00:00.000Z','endDate': None,'studyType': 'Prueba Tipo 2'})
#     assert resp.status_code == 400


# def test_actualiza_informacion_academica_id_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.patch(
#         '/empresa/' + '1234' + '/informacionAcademica/' + str(id_informacion_academica), json={'title': "Prueba Titulo 1",'institution': 'Prueba Institution 1','beginDate': '2008-04-15T00:00:00.000Z','endDate': None,'studyType': 'Prueba Tipo 2'})
#     assert resp.status_code == 404
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + '1234', json={'title': "Prueba Titulo 1",'institution': 'Prueba Institution 1','beginDate': '2008-04-15T00:00:00.000Z','endDate': None,'studyType': 'Prueba Tipo 2'})
#     assert resp.status_code == 404

# def test_actualiza_informacion_academica_datos_incompletos(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + str(id_informacion_academica), json={'title': ""})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + str(id_informacion_academica), json={'institution': ''})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + str(id_informacion_academica), json={'beginDate': None})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + str(id_informacion_academica), json={'studyType': ''})
#     assert resp.status_code == 400


# def test_obtiene_informacion_academica(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.get(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica')
#     assert resp.status_code == 200
#     jsonreponse = resp.json
#     assert jsonreponse[0]['title'] == 'Prueba Titulo 1'


# def test_obtiene_informacion_academica_empresa_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.get(
#         '/empresa/' + '123' + '/informacionAcademica')
#     assert resp.status_code == 404

# def test_obtiene_informacion_academica_id(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.get(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + str(id_informacion_academica))
#     assert resp.status_code == 200
#     assert resp.json.get('title') == 'Prueba Titulo 1'

# def test_obtiene_informacion_academica_id_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.get(
#         '/empresa/' + '1234' + '/informacionAcademica/' + str(id_informacion_academica))
#     assert resp.status_code == 404
#     resp = client.get(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + '1234')
#     assert resp.status_code == 404


# def test_elimina_informacion_academica(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.delete(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + str(id_informacion_academica))
#     assert resp.status_code == 204

# def test_elimina_informacion_academica_id_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_academica
#     resp = client.delete(
#         '/empresa/' + '1234' + '/informacionAcademica/' + str(id_informacion_academica))
#     assert resp.status_code == 404
#     resp = client.delete(
#         '/empresa/' + str(id_empresa) + '/informacionAcademica/' + '1234')
#     assert resp.status_code == 404


# # Pruebas Información Técnica

# def test_crea_informacion_tecnica(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.post(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica', json={'type': "Prueba Tipo",'description': 'Prueba Descripcion'})
#     assert resp.status_code == 201
#     assert resp.json.get('id')
#     id_informacion_tecnica = resp.json.get('id')

# def test_crea_informacion_tecnica_datos_incompletos(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.post(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica', json={'type': "Prueba Tipo"})
#     assert resp.status_code == 400
#     resp = client.post(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica', json={'type': "Prueba Tipo",'description': ''})
#     assert resp.status_code == 400

# def test_crea_informacion_tecnica_empresa_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.post(
#         '/empresa/123456/informacionTecnica', json={'type': "Prueba Tipo",'description': 'Prueba Descripcion'})
#     assert resp.status_code == 404
#     resp = client.post(
#         '/empresa/ddddd/informacionTecnica', json={'type': "Prueba Tipo",'description': 'Prueba Descripcion'})
#     assert resp.status_code == 400

# def test_actualiza_informacion_tecnica(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica/' + str(id_informacion_tecnica), json={'type': "Prueba Tipo 1",'description': 'Prueba Descripcion 1'})
#     assert resp.status_code == 200
#     assert resp.json.get('type') == 'Prueba Tipo 1'
#     assert resp.json.get('description') == 'Prueba Descripcion 1'



# def test_actualiza_informacion_tecnica_id_no_numeric(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.patch(
#         '/empresa/' + 'dddd' + '/informacionTecnica/' + str(id_informacion_tecnica), json={'type': "Prueba Tipo 1",'description': 'Prueba Descripcion 1'})
#     assert resp.status_code == 400
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica/' + '5ddd', json={'type': "Prueba Tipo 1",'description': 'Prueba Descripcion 1'})
#     assert resp.status_code == 400


# def test_actualiza_informacion_tecnica_id_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.patch(
#         '/empresa/' + '1234' + '/informacionTecnica/' + str(id_informacion_tecnica), json={'type': "Prueba Tipo 1",'description': 'Prueba Descripcion 1'})
#     assert resp.status_code == 404
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica/' + '1234', json={'type': "Prueba Tipo 1",'description': 'Prueba Descripcion 1'})
#     assert resp.status_code == 404

# def test_actualiza_informacion_tecnica_datos_incompletos(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica/' + str(id_informacion_tecnica), json={'type': ""})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica/' + str(id_informacion_tecnica), json={'description': ''})
#     assert resp.status_code == 400


# def test_obtiene_informacion_tecnica(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.get(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica')
#     assert resp.status_code == 200
#     jsonreponse = resp.json
#     assert jsonreponse[0]['type'] == 'Prueba Tipo 1'


# def test_obtiene_informacion_tecnica_empresa_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.get(
#         '/empresa/' + '123' + '/informacionTecnica')
#     assert resp.status_code == 404

# def test_obtiene_informacion_tecnica_id(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.get(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica/' + str(id_informacion_tecnica))
#     assert resp.status_code == 200
#     assert resp.json.get('type') == 'Prueba Tipo 1'

# def test_obtiene_informacion_tecnica_id_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.get(
#         '/empresa/' + '1234' + '/informacionTecnica/' + str(id_informacion_tecnica))
#     assert resp.status_code == 404
#     resp = client.get(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica/' + '1234')
#     assert resp.status_code == 404


# def test_elimina_informacion_tecnica(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.delete(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica/' + str(id_informacion_tecnica))
#     assert resp.status_code == 204

# def test_elimina_informacion_tecnica_id_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_tecnica
#     resp = client.delete(
#         '/empresa/' + '1234' + '/informacionTecnica/' + str(id_informacion_tecnica))
#     assert resp.status_code == 404
#     resp = client.delete(
#         '/empresa/' + str(id_empresa) + '/informacionTecnica/' + '1234')
#     assert resp.status_code == 404


# # Pruebas Información Laboral

# def test_crea_informacion_laboral(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.post(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral', json={'position': "Prueba Cargo",'organization': 'Prueba empresa', 'activities': 'Estas son algunas actividades', 'dateFrom': '2003-03-15T00:00:00.000Z'})
#     assert resp.status_code == 201
#     assert resp.json.get('id')
#     id_informacion_laboral = resp.json.get('id')

# def test_crea_informacion_laboral_datos_incompletos(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.post(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral', json={'position': "Prueba Cargo",'organization': 'Prueba empresa', 'dateFrom': '2003-03-15T00:00:00.000Z'})
#     assert resp.status_code == 400
#     resp = client.post(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral', json={'position': "Prueba Cargo",'organization': '', 'activities': 'Estas son algunas actividades', 'dateFrom': '2003-03-15T00:00:00.000Z'})
#     assert resp.status_code == 400

# def test_crea_informacion_laboral_empresa_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.post(
#         '/empresa/123456/informacionLaboral', json={'position': "Prueba Cargo",'organization': 'Prueba empresa', 'activities': 'Estas son algunas actividades', 'dateFrom': '2003-03-15T00:00:00.000Z'})
#     assert resp.status_code == 404
#     resp = client.post(
#         '/empresa/ddddd/informacionLaboral', json={'position': "Prueba Cargo",'organization': 'Prueba empresa', 'activities': 'Estas son algunas actividades', 'dateFrom': '2003-03-15T00:00:00.000Z'})
#     assert resp.status_code == 400

# def test_actualiza_informacion_laboral(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + str(id_informacion_laboral), json={'position': 'Prueba Cargo 2','organization': 'Prueba empresa 2', 'activities': 'Estas son algunas actividades 2', 'dateFrom': '2004-03-15T00:00:00.000Z', 'dateTo' : None})
#     assert resp.status_code == 200
#     assert resp.json.get('position') == 'Prueba Cargo 2'
#     assert resp.json.get('organization') == 'Prueba empresa 2'
#     assert resp.json.get('activities') == 'Estas son algunas actividades 2'



# def test_actualiza_informacion_laboral_id_no_numeric(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.patch(
#         '/empresa/' + 'dddd' + '/informacionLaboral/' + str(id_informacion_laboral), json={'position': 'Prueba Cargo 2','organization': 'Prueba empresa 2', 'activities': 'Estas son algunas actividades 2', 'dateFrom': '2004-03-15T00:00:00.000Z', 'dateTo' : None})
#     assert resp.status_code == 400
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + '5ddd', json={'position': 'Prueba Cargo 2','organization': 'Prueba empresa 2', 'activities': 'Estas son algunas actividades 2', 'dateFrom': '2004-03-15T00:00:00.000Z', 'dateTo' : None})
#     assert resp.status_code == 400


# def test_actualiza_informacion_laboral_id_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.patch(
#         '/empresa/' + '1234' + '/informacionLaboral/' + str(id_informacion_laboral), json={'position': 'Prueba Cargo 2','organization': 'Prueba empresa 2', 'activities': 'Estas son algunas actividades 2', 'dateFrom': '2004-03-15T00:00:00.000Z', 'dateTo' : None})
#     assert resp.status_code == 404
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + '1234', json={'position': 'Prueba Cargo 2','organization': 'Prueba empresa 2', 'activities': 'Estas son algunas actividades 2', 'dateFrom': '2004-03-15T00:00:00.000Z', 'dateTo' : None})
#     assert resp.status_code == 404

# def test_actualiza_informacion_laboral_datos_incompletos(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + str(id_informacion_laboral), json={'position': ""})
#     assert resp.status_code == 400

#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + str(id_informacion_laboral), json={'organization': ''})
#     assert resp.status_code == 400
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + str(id_informacion_laboral), json={'activities': ''})
#     assert resp.status_code == 400
#     resp = client.patch(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + str(id_informacion_laboral), json={'dateFrom': ''})
#     assert resp.status_code == 400


# def test_obtiene_informacion_laboral(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.get(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral')
#     assert resp.status_code == 200
#     jsonreponse = resp.json
#     assert jsonreponse[0]['position'] == 'Prueba Cargo 2'


# def test_obtiene_informacion_laboral_empresa_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.get(
#         '/empresa/' + '123' + '/informacionLaboral')
#     assert resp.status_code == 404

# def test_obtiene_informacion_laboral_id(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.get(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + str(id_informacion_laboral))
#     assert resp.status_code == 200
#     assert resp.json.get('position') == 'Prueba Cargo 2'

# def test_obtiene_informacion_laboral_id_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.get(
#         '/empresa/' + '1234' + '/informacionLaboral/' + str(id_informacion_laboral))
#     assert resp.status_code == 404
#     resp = client.get(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + '1234')
#     assert resp.status_code == 404


# def test_elimina_informacion_laboral(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.delete(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + str(id_informacion_laboral))
#     assert resp.status_code == 204

# def test_elimina_informacion_laboral_id_no_existe(client: FlaskClient):
#     global id_empresa, id_informacion_laboral
#     resp = client.delete(
#         '/empresa/' + '1234' + '/informacionLaboral/' + str(id_informacion_laboral))
#     assert resp.status_code == 404
#     resp = client.delete(
#         '/empresa/' + str(id_empresa) + '/informacionLaboral/' + '1234')
#     assert resp.status_code == 404
    
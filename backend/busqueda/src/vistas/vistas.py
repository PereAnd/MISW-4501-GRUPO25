from flask_restful import Resource
from flask import request
from ..modelos import db, Busqueda, BusquedaEschema, Resultado, ResultadoEschema
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys, os



busqueda_schema = BusquedaEschema()
resultado_schema = ResultadoEschema()

# Busquedaes
# Vista POST - GET
class VistaBusquedaes(Resource):


    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL")) + "/empresa"
        self.urlBackEnd2 = str(os.getenv("CAND_BACK_URL")) + "/candidato"

    def post(self,empresaId,proyectoId,perfilId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 
        
        try:
            nuevo_busqueda = Busqueda(
                                        searchDate=datetime.now(),
                                        status="INIT",
                                        perfilId=perfilId,
                                        proyectoId=proyectoId,
                                        empresaId=empresaId)

            db.session.add(nuevo_busqueda)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return busqueda_schema.dump(nuevo_busqueda), 201
    
    def get(self,empresaId,proyectoId,perfilId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 
        try:
                return[busqueda_schema.dump(t) for t in Busqueda.query.filter(
                Busqueda.perfilId == perfilId)], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412


# Busquedaes
# Vista PATCH - GET - DELETE
class VistaBusqueda(Resource):

    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL")) + "/empresa"

                
    def get(self, empresaId, proyectoId, perfilId, id):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            busqueda = Busqueda.query.get(id)
            if busqueda is None:
                return 'No existe la cuenta del busqueda solicitada', 404
            else:
                return busqueda_schema.dump(busqueda), 200
            

    def delete(self, empresaId, proyectoId, perfilId, id):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            busqueda = Busqueda.query.get(id)
            if busqueda is None:
                return 'No existe el busqueda solicitado', 404
        try:
            db.session.delete(busqueda)
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
            
# PING
# Vista GET
class VistaPing(Resource):
    def get(self):
        return "pong"            

# Resultado
# Vista POST - GET

class VistaResultados(Resource):
    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL")) + "/empresa"
        self.urlBackEnd2 = str(os.getenv("CAND_BACK_URL")) + "/candidato"

    def post(self, empresaId, proyectoId, perfilId, busquedaId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 
        

        candidatoId = request.json["candidatoId"]
        if isinstance(candidatoId, str):
            if candidatoId.isnumeric() == False:
                return 'El id del candidato no es un número.', 400

        response = requests.get(self.urlBackEnd2 + "/" + str(candidatoId))
        if response.status_code != 200:
            return response.text, response.status_code 



        if busquedaId.isnumeric() == False:
            return 'El busquedaId no es un número.', 400
        else:
            busqueda = Busqueda.query.get(busquedaId)
            if busqueda is None:
                return 'No existe la cuenta del busqueda solicitada', 404

        try:
            nueva_resultado = Resultado(
                                        perfilId=perfilId,
                                        proyectoId=proyectoId,
                                        empresaId=empresaId,
                                        busquedaId=busquedaId,
                                        candidatoId=candidatoId)
            db.session.add(nueva_resultado)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return resultado_schema.dump(nueva_resultado), 201
    
    def get(self, empresaId, proyectoId, perfilId, busquedaId):

        if empresaId.isnumeric() == False:
            return 'El id de la empresa no es un número.', 400
        if proyectoId.isnumeric() == False:
            return 'El id del proyecto no es un número.', 400
        else:
            response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
            if response.status_code != 200:
                return response.text, response.status_code 

        if busquedaId.isnumeric() == False:
            return 'El busquedaId no es un número.', 400
        else:
            busqueda = Busqueda.query.get(busquedaId)
            if busqueda is None:
                return 'No existe la cuenta del busqueda solicitada', 404
            
        try:
                return[resultado_schema.dump(t) for t in Resultado.query.filter(
                (Resultado.busquedaId == busquedaId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        

        
# Resultado
# Vista PATCH - GET - DELETE
class VistaResultado(Resource):
    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL")) + "/empresa"
                
    def get(self, empresaId, proyectoId, perfilId, busquedaId, id):


        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if busquedaId.isnumeric() == False:
            return 'El busquedaId no es un número.', 400
        else:
            busqueda = Busqueda.query.get(busquedaId)
            if busqueda is None:
                return 'No existe la cuenta del busqueda solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            resultado = Resultado.query.get(id)
            if resultado is None:
                return 'No existe la Resultado del busqueda solicitada', 404
        return resultado_schema.dump(resultado), 200

    def delete(self, empresaId, proyectoId, perfilId, busquedaId, id):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if busquedaId.isnumeric() == False:
            return 'El busquedaId no es un número.', 400
        else:
            busqueda = Busqueda.query.get(busquedaId)
            if busqueda is None:
                return 'No existe la cuenta del busqueda solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            resultado = Resultado.query.get(id)
            if resultado is None:
                return 'No existe la Resultado del busqueda solicitada', 404
        try:
            db.session.delete(resultado)
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        

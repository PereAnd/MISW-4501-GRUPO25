from flask_restful import Resource
from flask import request
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys
import os



class VistaRegistro(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def post(self):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd , json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
        
    def get(self):
        #try:
            return self.breaker.make_remote_call_get(self.urlBackEnd , params=request.args.to_dict())
            #return 'Correcto', 200
        #except Exception:
            #return 'ocurrió un error', 412
            #return {'Error': str(sys.exc_info()[0])}, 412

# Empresas
# Vista PATCH - GET
class VistaEmpresa(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"
    def patch(self, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + "/" + id , json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
        
            
# PING
# Vista GET
class VistaPing(Resource):
    def get(self):
        return "pong"            
    

# Vertical
# Vista POST - GET

class VistaVerticales(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def post(self, empresaId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + "/" + empresaId + "/vertical", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def get(self, empresaId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/vertical", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

        
# Vertical
# Vista PATCH - GET - DELETE
class VistaVertical(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def patch(self, empresaId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + "/" + empresaId + "/vertical/" + id, json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

                
    def get(self, empresaId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/vertical/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def delete(self, empresaId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + "/" + empresaId + "/vertical/"+ id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


# Ubicacion
# Vista POST - GET

class VistaUbicaciones(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def post(self, empresaId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + "/" + empresaId + "/ubicacion", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def get(self, empresaId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/ubicacion", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

        
# Ubicacion
# Vista PATCH - GET - DELETE
class VistaUbicacion(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def patch(self, empresaId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + "/" + empresaId + "/ubicacion/" + id, json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

                
    def get(self, empresaId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/ubicacion/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def delete(self, empresaId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + "/" + empresaId + "/ubicacion/"+ id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412



# Proyecto
# Vista POST - GET

class VistaProyectos(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def post(self, empresaId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + "/" + empresaId + "/proyecto", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def get(self, empresaId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/proyecto", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

        
# Proyecto
# Vista PATCH - GET - DELETE
class VistaProyecto(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def patch(self, empresaId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + "/" + empresaId + "/proyecto/" + id, json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

                
    def get(self, empresaId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/proyecto/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def delete(self, empresaId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + "/" + empresaId + "/proyecto/"+ id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412



# Entrevistas
# Vista POST - GET
class VistaEntrevistas(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def get(self, empresaId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/entrevista", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


# Aplicaciones
# Vista POST - GET
class VistaAplicaciones(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def get(self, empresaId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/aplicacion", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412



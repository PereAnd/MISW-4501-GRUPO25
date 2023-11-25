from flask_restful import Resource
from flask import request
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys
import os



class VistaBusquedaes(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("BUSQ_BACK_URL"))

    def post(self,empresaId,proyectoId,perfilId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/busqueda")
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
        
    def get(self,empresaId,proyectoId,perfilId):
        #try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/busqueda", params=request.args.to_dict())
            #return 'Correcto', 200
        #except Exception:
            #return 'ocurrió un error', 412
            #return {'Error': str(sys.exc_info()[0])}, 412

# Busquedaes
# Vista PATCH - GET
class VistaBusqueda(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("BUSQ_BACK_URL"))

    def get(self,empresaId,proyectoId,perfilId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/busqueda/" + id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
        
    def delete(self,empresaId,proyectoId,perfilId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/busqueda/" + id)
        except Exception:
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
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("BUSQ_BACK_URL"))

    def post(self,empresaId,proyectoId,perfilId, busquedaId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/busqueda/" + busquedaId + "/resultado", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def get(self,empresaId,proyectoId,perfilId, busquedaId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/busqueda/" + busquedaId + "/resultado", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

        
# Resultado
# Vista PATCH - GET - DELETE
class VistaResultado(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("BUSQ_BACK_URL"))

                
    def get(self,empresaId,proyectoId,perfilId, busquedaId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/busqueda/" + busquedaId + "/resultado/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def delete(self,empresaId,proyectoId,perfilId, busquedaId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/busqueda/" + busquedaId + "/resultado/"+ id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


#Ejecución asincronica
class VistaEjecuta(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("BUSQ_BACK_URL"))

    def post(self, empresaId, proyectoId, perfilId, id):       
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/busqueda/" + id + "/run", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
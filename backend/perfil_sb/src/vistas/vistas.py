from flask_restful import Resource
from flask import request
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys
import os



class VistaPerfiles(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL"))

    def post(self,empresaId,proyectoId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
        
    def get(self,empresaId,proyectoId):
        #try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil", params=request.args.to_dict())
            #return 'Correcto', 200
        #except Exception:
            #return 'ocurrió un error', 412
            #return {'Error': str(sys.exc_info()[0])}, 412

# Perfiles
# Vista PATCH - GET
class VistaPerfil(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL"))

    def patch(self,empresaId,proyectoId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + id , json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self,empresaId,proyectoId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
        
    def delete(self,empresaId,proyectoId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
        
            
# PING
# Vista GET
class VistaPing(Resource):
    def get(self):
        return "pong"            
    

# Habilidad
# Vista POST - GET

class VistaHabilidades(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL"))

    def post(self,empresaId,proyectoId, perfilId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/habilidad", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def get(self,empresaId,proyectoId, perfilId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/habilidad", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

        
# Habilidad
# Vista PATCH - GET - DELETE
class VistaHabilidad(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL"))

    def patch(self,empresaId,proyectoId, perfilId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/habilidad/" + id, json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

                
    def get(self,empresaId,proyectoId, perfilId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/habilidad/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def delete(self,empresaId,proyectoId, perfilId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/habilidad/"+ id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

# Conocimiento
# Vista POST - GET

class VistaConocimientos(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL"))

    def post(self,empresaId,proyectoId, perfilId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/conocimiento", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def get(self,empresaId,proyectoId, perfilId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/conocimiento", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

        
# Conocimiento
# Vista PATCH - GET - DELETE
class VistaConocimiento(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL"))

    def patch(self,empresaId,proyectoId, perfilId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/conocimiento/" + id, json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

                
    def get(self,empresaId,proyectoId, perfilId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/conocimiento/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def delete(self,empresaId,proyectoId, perfilId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/conocimiento/"+ id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

# Idioma
# Vista POST - GET

class VistaIdiomas(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL"))

    def post(self,empresaId,proyectoId, perfilId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/idioma", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def get(self,empresaId,proyectoId, perfilId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/idioma", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

        
# Idioma
# Vista PATCH - GET - DELETE
class VistaIdioma(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL"))

    def patch(self,empresaId,proyectoId, perfilId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/idioma/" + id, json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

                
    def get(self,empresaId,proyectoId, perfilId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/idioma/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def delete(self,empresaId,proyectoId, perfilId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/idioma/"+ id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

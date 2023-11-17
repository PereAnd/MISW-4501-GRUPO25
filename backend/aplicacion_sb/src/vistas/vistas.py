from flask_restful import Resource
from flask import request
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys
import os



class VistaAplicaciones(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("APLI_BACK_URL"))

    def post(self,empresaId,proyectoId,perfilId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/aplicacion", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
        
    def get(self,empresaId,proyectoId,perfilId):
        #try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/aplicacion", params=request.args.to_dict())
            #return 'Correcto', 200
        #except Exception:
            #return 'ocurrió un error', 412
            #return {'Error': str(sys.exc_info()[0])}, 412

# Aplicaciones
# Vista PATCH - GET
class VistaAplicacion(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("APLI_BACK_URL"))

    def patch(self,empresaId,proyectoId,perfilId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/aplicacion/" + id , json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self,empresaId,proyectoId,perfilId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/aplicacion/" + id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
        
    def delete(self,empresaId,proyectoId,perfilId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/aplicacion/" + id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
        
            
# PING
# Vista GET
class VistaPing(Resource):
    def get(self):
        return "pong"            
    

# Entrevista
# Vista POST - GET

class VistaEntrevistas(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("APLI_BACK_URL"))

    def post(self,empresaId,proyectoId,perfilId, aplicacionId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/aplicacion/" + aplicacionId + "/entrevista", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def get(self,empresaId,proyectoId,perfilId, aplicacionId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/aplicacion/" + aplicacionId + "/entrevista", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

        
# Entrevista
# Vista PATCH - GET - DELETE
class VistaEntrevista(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("APLI_BACK_URL"))

    def patch(self,empresaId,proyectoId,perfilId, aplicacionId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/aplicacion/" + aplicacionId + "/entrevista/" + id, json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

                
    def get(self,empresaId,proyectoId,perfilId, aplicacionId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/aplicacion/" + aplicacionId + "/entrevista/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def delete(self,empresaId,proyectoId,perfilId, aplicacionId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + '/empresa/' + empresaId + '/proyecto/' + proyectoId + "/perfil/" + perfilId + "/aplicacion/" + aplicacionId + "/entrevista/"+ id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


# Entrevistas - Candidato
# Vista GET
class VistaEntrevistasCandidato(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("APLI_BACK_URL"))

    def get(self,candidatoId,aplicacionId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/candidato/' + candidatoId + "/aplicacion/" + aplicacionId + "/entrevista", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412



# Entrevista - Candidato
# Vista GET
class VistaEntrevistaCandidato(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("APLI_BACK_URL"))

    def get(self, candidatoId,aplicacionId,id):

        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/candidato/' + candidatoId + "/aplicacion/" + aplicacionId + "/entrevista/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


# Aplicaciones - Candidato
# Vista GET
class VistaAplicacionesCandidato(Resource):


    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("APLI_BACK_URL"))
    
    def get(self,candidatoId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/candidato/' + candidatoId + "/aplicacion", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


# Aplicacion - Candidato
# Vista GET
class VistaAplicacionCandidato(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("APLI_BACK_URL"))
                
    def get(self, candidatoId, id):

        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + '/candidato/' + candidatoId + "/aplicacion/" + id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412
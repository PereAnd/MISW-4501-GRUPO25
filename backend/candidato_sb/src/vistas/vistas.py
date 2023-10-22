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
        self.urlBackEnd = str(os.getenv("CAND_BACK_URL")) + "/candidatobe"

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

# Candidatos
# Vista PATCH - GET
class VistaCandidato(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("CAND_BACK_URL")) + "/candidatobe"
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

# Informacion Academica
# Vista POST - GET

class VistaInformacionesAcademicas(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("CAND_BACK_URL")) + "/candidatobe"

    def post(self, candidatoId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + "/" + candidatoId + "/informacionAcademica", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def get(self, candidatoId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + candidatoId + "/informacionAcademica", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

        
# Informacion Academica
# Vista PATCH - GET - DELETE
class VistaInformacionAcademica(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("CAND_BACK_URL")) + "/candidatobe"

    def patch(self, candidatoId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + "/" + candidatoId + "/informacionAcademica/" + id, json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

                
    def get(self, candidatoId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + candidatoId + "/informacionAcademica/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def delete(self, candidatoId, id):
        try:
            return self.breaker.make_remote_call_delete(self.urlBackEnd + "/" + candidatoId + "/informacionAcademica/"+ id)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


# Informacion Tecnica
# Vista POST - GET
class VistaInformacionesTecnicas(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("CAND_BACK_URL")) + "/candidatobe"

    def post(self, candidatoId):
        try:
            return self.breaker.make_remote_call_post(self.urlBackEnd + "/" + candidatoId + "/informacionTecnica", json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def get(self, candidatoId):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + candidatoId + "/informacionTecnica", params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

        
# Informacion Tecnica
# Vista PATCH - GET - DELETE
class VistaInformacionTecnica(Resource):

    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.breaker = kwargs['breaker']
        self.urlBackEnd = str(os.getenv("CAND_BACK_URL")) + "/candidatobe"


    def patch(self, candidatoId, id):
        try:
            return self.breaker.make_remote_call_patch(self.urlBackEnd + "/" + candidatoId + "/informacionTecnica/" + id, json=request.json)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412

                
    def get(self, candidatoId, id):
        try:
            return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + candidatoId + "/informacionTecnica/"+ id, params=request.args.to_dict())
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


    def delete(self, candidatoId, id):
        try:
            url = self.urlBackEnd + "/" + candidatoId + "/informacionTecnica/"+ id
#            requests.delete(self.urlBackEnd + "/" + candidatoId + "/informacionTecnica/"+ id)
#            return "Correcto", 204
            return self.breaker.make_remote_call_delete(url)
        except Exception:
            return {'Error': str(sys.exc_info()[0])}, 412


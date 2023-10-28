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

# # Informacion Academica
# # Vista POST - GET

# class VistaInformacionesAcademicas(Resource):

#     def __init__(self, **kwargs):
#         # smart_engine is a black box dependency
#         self.breaker = kwargs['breaker']
#         self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

#     def post(self, empresaId):
#         try:
#             return self.breaker.make_remote_call_post(self.urlBackEnd + "/" + empresaId + "/informacionAcademica", json=request.json)
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412


#     def get(self, empresaId):
#         try:
#             return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/informacionAcademica", params=request.args.to_dict())
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412

        
# # Informacion Academica
# # Vista PATCH - GET - DELETE
# class VistaInformacionAcademica(Resource):
#     def __init__(self, **kwargs):
#         # smart_engine is a black box dependency
#         self.breaker = kwargs['breaker']
#         self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

#     def patch(self, empresaId, id):
#         try:
#             return self.breaker.make_remote_call_patch(self.urlBackEnd + "/" + empresaId + "/informacionAcademica/" + id, json=request.json)
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412

                
#     def get(self, empresaId, id):
#         try:
#             return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/informacionAcademica/"+ id, params=request.args.to_dict())
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412


#     def delete(self, empresaId, id):
#         try:
#             return self.breaker.make_remote_call_delete(self.urlBackEnd + "/" + empresaId + "/informacionAcademica/"+ id)
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412


# # Informacion Tecnica
# # Vista POST - GET
# class VistaInformacionesTecnicas(Resource):
#     def __init__(self, **kwargs):
#         # smart_engine is a black box dependency
#         self.breaker = kwargs['breaker']
#         self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

#     def post(self, empresaId):
#         try:
#             return self.breaker.make_remote_call_post(self.urlBackEnd + "/" + empresaId + "/informacionTecnica", json=request.json)
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412


#     def get(self, empresaId):
#         try:
#             return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/informacionTecnica", params=request.args.to_dict())
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412

        
# # Informacion Tecnica
# # Vista PATCH - GET - DELETE
# class VistaInformacionTecnica(Resource):

#     def __init__(self, **kwargs):
#         # smart_engine is a black box dependency
#         self.breaker = kwargs['breaker']
#         self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"


#     def patch(self, empresaId, id):
#         try:
#             return self.breaker.make_remote_call_patch(self.urlBackEnd + "/" + empresaId + "/informacionTecnica/" + id, json=request.json)
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412

                
#     def get(self, empresaId, id):
#         try:
#             return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/informacionTecnica/"+ id, params=request.args.to_dict())
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412


#     def delete(self, empresaId, id):
#         try:
#             url = self.urlBackEnd + "/" + empresaId + "/informacionTecnica/"+ id
# #            requests.delete(self.urlBackEnd + "/" + empresaId + "/informacionTecnica/"+ id)
# #            return "Correcto", 204
#             return self.breaker.make_remote_call_delete(url)
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412

# # Informacion Laboral
# # Vista POST - GET
# class VistaInformacionesLaborales(Resource):
#     def __init__(self, **kwargs):
#         # smart_engine is a black box dependency
#         self.breaker = kwargs['breaker']
#         self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

#     def post(self, empresaId):
#         try:
#             return self.breaker.make_remote_call_post(self.urlBackEnd + "/" + empresaId + "/informacionLaboral", json=request.json)
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412


#     def get(self, empresaId):
#         try:
#             return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/informacionLaboral", params=request.args.to_dict())
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412

        
# # Informacion Laboral
# # Vista PATCH - GET - DELETE
# class VistaInformacionLaboral(Resource):

#     def __init__(self, **kwargs):
#         # smart_engine is a black box dependency
#         self.breaker = kwargs['breaker']
#         self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"


#     def patch(self, empresaId, id):
#         try:
#             return self.breaker.make_remote_call_patch(self.urlBackEnd + "/" + empresaId + "/informacionLaboral/" + id, json=request.json)
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412

                
#     def get(self, empresaId, id):
#         try:
#             return self.breaker.make_remote_call_get(self.urlBackEnd + "/" + empresaId + "/informacionLaboral/"+ id, params=request.args.to_dict())
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412


#     def delete(self, empresaId, id):
#         try:
#             url = self.urlBackEnd + "/" + empresaId + "/informacionLaboral/"+ id
# #            requests.delete(self.urlBackEnd + "/" + empresaId + "/informacionLaboral/"+ id)
# #            return "Correcto", 204
#             return self.breaker.make_remote_call_delete(url)
#         except Exception:
#             return {'Error': str(sys.exc_info()[0])}, 412


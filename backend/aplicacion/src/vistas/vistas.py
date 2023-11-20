from flask_restful import Resource
from flask import request
from modelos import db, Aplicacion, AplicacionEschema, Entrevista, EntrevistaEschema
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys, os



aplicacion_schema = AplicacionEschema()
entrevista_schema = EntrevistaEschema()

# Aplicaciones
# Vista POST - GET
class VistaAplicaciones(Resource):


    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL")) + "/empresa"
        self.urlBackEnd2 = str(os.getenv("CAND_BACK_URL")) + "/candidato"

    def post(self,empresaId,proyectoId,perfilId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if not "applicationDate" in request.json or not "status" in request.json or not "candidatoId" in request.json:
            return 'Los campos applicationDate, candidatoId y status son requeridos', 400

        candidatoId = request.json["candidatoId"]
        if isinstance(candidatoId, str):
            if candidatoId.isnumeric() == False:
                return 'El id del candidato no es un número.', 400

        response = requests.get(self.urlBackEnd2 + "/" + str(candidatoId))

        if response.status_code != 200:
            return response.text, response.status_code 

        result = None
        if "result" in request.json:
            result = request.json["result"]
        
        try:
            applicationDate = datetime.strptime(request.json["applicationDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            return "El campo applicationDate no tiene formato de fecha correcto", 400

        try:
            nuevo_aplicacion = Aplicacion(
                                        applicationDate=applicationDate,
                                        status=request.json["status"],
                                        perfilId=perfilId,
                                        proyectoId=proyectoId,
                                        empresaId=empresaId,
                                        candidatoId=candidatoId,
                                        result=result)

            db.session.add(nuevo_aplicacion)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return aplicacion_schema.dump(nuevo_aplicacion), 201
    
    def get(self,empresaId,proyectoId,perfilId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 
        try:
                return[aplicacion_schema.dump(t) for t in Aplicacion.query.filter(
                Aplicacion.perfilId == perfilId)], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412


# Aplicaciones
# Vista PATCH - GET - DELETE
class VistaAplicacion(Resource):

    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL")) + "/empresa"

    def patch(self, empresaId, proyectoId, perfilId, id):


        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 
            
        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            aplicacion = Aplicacion.query.get(id)
            if aplicacion is None:
                return 'No existe la cuenta del aplicacion solicitada', 404
            else:


                if "applicationDate" in request.json:
                    if request.json["applicationDate"] == "":
                        db.session.rollback()
                        return 'El campo applicationDate es requerido', 400
                    try:
                        birthDate = datetime.strptime(request.json["applicationDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
                    except:
                        db.session.rollback()
                        return "El campo applicationDate no tiene formato de fecha correcto", 400
                    aplicacion.applicationDate = birthDate


                if "status" in request.json:
                    if request.json["status"] == "":
                        return 'El campo status es requerido', 400
                    aplicacion.status = request.json["status"]

                if "result" in request.json:
                    aplicacion.result = request.json["result"]
                    
                try:
                    db.session.commit()
                    return aplicacion_schema.dump(aplicacion), 200
                except:
                    db.session.rollback()
                    return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, empresaId, proyectoId, perfilId, id):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            aplicacion = Aplicacion.query.get(id)
            if aplicacion is None:
                return 'No existe la cuenta del aplicacion solicitada', 404
            else:
                return aplicacion_schema.dump(aplicacion), 200
            

    def delete(self, empresaId, proyectoId, perfilId, id):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            aplicacion = Aplicacion.query.get(id)
            if aplicacion is None:
                return 'No existe el aplicacion solicitado', 404
        try:
            db.session.delete(aplicacion)
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

# Entrevista
# Vista POST - GET

class VistaEntrevistas(Resource):
    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL")) + "/empresa"

    def post(self, empresaId, proyectoId, perfilId, aplicacionId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 


        if aplicacionId.isnumeric() == False:
            return 'El aplicacionId no es un número.', 400
        else:
            aplicacion = Aplicacion.query.get(aplicacionId)
            if aplicacion is None:
                return 'No existe la cuenta del aplicacion solicitada', 404

        if not "enterviewDate" in request.json or not "done" in request.json:
            return 'Los campos enterviewDate, done son requeridos', 400
        if request.json["enterviewDate"] == "" or request.json["done"] == "": 
            return 'Los campos enterviewDate, done son requeridos', 400
        
        done = request.json["done"]
        if not isinstance(done, bool):
            return "El campo done no tiene formato boolean", 400
        
        feedback = None
        if "feedback" in request.json: 
            feedback = request.json["feedback"]

        try:
            enterviewDate = datetime.strptime(request.json["enterviewDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            return "El campo enterviewDate no tiene formato de fecha correcto", 400



        try:
            nueva_entrevista = Entrevista(enterviewDate=enterviewDate, 
                                        done=done,
                                        feedback=feedback,
                                        perfilId=perfilId,
                                        proyectoId=proyectoId,
                                        empresaId=empresaId,
                                        aplicacionId=aplicacionId)
            db.session.add(nueva_entrevista)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return entrevista_schema.dump(nueva_entrevista), 201
    
    def get(self, empresaId, proyectoId, perfilId, aplicacionId):


        if empresaId.isnumeric() == False:
            return 'El id de la empresa no es un número.', 400
        if proyectoId.isnumeric() == False:
            return 'El id del proyecto no es un número.', 400
        else:
            response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
            if response.status_code != 200:
                return response.text, response.status_code 

        if aplicacionId.isnumeric() == False:
            return 'El aplicacionId no es un número.', 400
        else:
            aplicacion = Aplicacion.query.get(aplicacionId)
            if aplicacion is None:
                return 'No existe la cuenta del aplicacion solicitada', 404
            
        try:
                return[entrevista_schema.dump(t) for t in Entrevista.query.filter(
                (Entrevista.aplicacionId == aplicacionId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        

        
# Entrevista
# Vista PATCH - GET - DELETE
class VistaEntrevista(Resource):
    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("PERF_BACK_URL")) + "/empresa"

    def patch(self, empresaId, proyectoId, perfilId, aplicacionId, id):
        

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 



        if aplicacionId.isnumeric() == False:
            return 'El aplicacionId no es un número.', 400
        else:
            aplicacion = Aplicacion.query.get(aplicacionId)
            if aplicacion is None:
                return 'No existe la cuenta del aplicacion solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            entrevista = Entrevista.query.get(id)
            if entrevista is None:
                return 'No existe la Entrevista del aplicacion solicitada', 404


            if "done" in request.json:
                done = request.json["done"]
                if not isinstance(done, bool):
                    db.session.rollback()
                    return "El campo done no tiene formato boolean", 400
                
                entrevista.done = request.json["done"]

            if "enterviewDate" in request.json:
                if request.json["enterviewDate"] == "":
                    db.session.rollback()
                    return 'El campo enterviewDate es requerido', 400
                try:
                    enterviewDate = datetime.strptime(request.json["enterviewDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
                except:
                    db.session.rollback()
                    return "El campo enterviewDate no tiene formato de fecha correcto", 400
                entrevista.enterviewDate = enterviewDate

            if "feedback" in request.json:
                entrevista.feedback = request.json["feedback"]

            try:
                db.session.commit()
                return entrevista_schema.dump(entrevista), 200
            except:
                db.session.rollback()
                return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, empresaId, proyectoId, perfilId, aplicacionId, id):


        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if aplicacionId.isnumeric() == False:
            return 'El aplicacionId no es un número.', 400
        else:
            aplicacion = Aplicacion.query.get(aplicacionId)
            if aplicacion is None:
                return 'No existe la cuenta del aplicacion solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            entrevista = Entrevista.query.get(id)
            if entrevista is None:
                return 'No existe la Entrevista del aplicacion solicitada', 404
        return entrevista_schema.dump(entrevista), 200

    def delete(self, empresaId, proyectoId, perfilId, aplicacionId, id):


        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId + "/perfil/" + perfilId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if aplicacionId.isnumeric() == False:
            return 'El aplicacionId no es un número.', 400
        else:
            aplicacion = Aplicacion.query.get(aplicacionId)
            if aplicacion is None:
                return 'No existe la cuenta del aplicacion solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            entrevista = Entrevista.query.get(id)
            if entrevista is None:
                return 'No existe la Entrevista del aplicacion solicitada', 404
        try:
            db.session.delete(entrevista)
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
# Aplicaciones - Candidato
# Vista GET
class VistaAplicacionesCandidato(Resource):


    def __init__(self, **kwargs):
        self.urlBackEnd2 = str(os.getenv("CAND_BACK_URL")) + "/candidato"
    
    def get(self,candidatoId):

        response = requests.get(self.urlBackEnd2 + "/" + candidatoId)
        if response.status_code != 200:
            return response.text, response.status_code 
        try:
                return[aplicacion_schema.dump(t) for t in Aplicacion.query.filter(
                Aplicacion.candidatoId == candidatoId)], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412


# Aplicacion - Candidato
# Vista GET
class VistaAplicacionCandidato(Resource):

    def __init__(self, **kwargs):
        self.urlBackEnd2 = str(os.getenv("CAND_BACK_URL")) + "/candidato"
                
    def get(self, candidatoId, id):

        response = requests.get(self.urlBackEnd2 + "/" + candidatoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            aplicacion = Aplicacion.query.get(id)
            if aplicacion is None:
                return 'No existe la cuenta del aplicacion solicitada', 404
            else:
                return aplicacion_schema.dump(aplicacion), 200
            

# Entrevistas - Candidato
# Vista GET
class VistaEntrevistasCandidato(Resource):


    def __init__(self, **kwargs):
        self.urlBackEnd2 = str(os.getenv("CAND_BACK_URL")) + "/candidato"
    
    def get(self,candidatoId,aplicacionId):

        response = requests.get(self.urlBackEnd2 + "/" + candidatoId)
        if response.status_code != 200:
            return response.text, response.status_code 
        

        if aplicacionId.isnumeric() == False:
            return 'El id de la aplicacion no es un número.', 400
        try:
                return[entrevista_schema.dump(t) for t in Entrevista.query.filter(
                Entrevista.aplicacionId == aplicacionId)], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412


# Entrevista - Candidato
# Vista GET
class VistaEntrevistaCandidato(Resource):

    def __init__(self, **kwargs):
        self.urlBackEnd2 = str(os.getenv("CAND_BACK_URL")) + "/candidato"
                
    def get(self, candidatoId,aplicacionId,id):

        response = requests.get(self.urlBackEnd2 + "/" + candidatoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if aplicacionId.isnumeric() == False:
            return 'El id de la aplicacion no es un número.', 400
        
        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            entrevista = Entrevista.query.get(id)
            if entrevista is None:
                return 'No existe la entrevista solicitada', 404
            else:
                return entrevista_schema.dump(entrevista), 200



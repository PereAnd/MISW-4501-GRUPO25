from flask_restful import Resource
from flask import request
from ..modelos import db, Candidato, CandidatoEschema, InformacionAcademica, InformacionAcademicaEschema, InformacionTecnica, InformacionTecnicaEschema
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys

candidato_schema = CandidatoEschema()
informacion_schema = InformacionAcademicaEschema()
informacionTecnica_schema = InformacionTecnicaEschema


# Candidatos
# Vista POST - GET
class VistaRegistro(Resource):

    def post(self):
        if not "names" in request.json or not "lastNames" in request.json or not "mail" in request.json or not "password" in request.json or not "confirmPassword" in request.json:
            return 'Los campos names, lastNames, mail, password y confirmPassword son requeridos', 400

        if request.json["names"] == "" or request.json["lastNames"] == ""  or request.json["mail"] == ""  or request.json["password"] == ""  or request.json["confirmPassword"] == "" : 
            return 'Los campos names, lastNames, mail, password y confirmPassword son requeridos', 400

        if request.json["password"] != request.json["confirmPassword"]: 
            return 'El campo password y el campo confirmPassword deben ser requeridos', 400

        try:
            nuevo_candidato = Candidato(names=request.json["names"], 
                                        lastNames=request.json["lastNames"],
                                        mail=request.json["mail"],
                                        password=request.json["password"])

            db.session.add(nuevo_candidato)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        return {'id':nuevo_candidato.id, 'names ': nuevo_candidato.names, 'lastNames': nuevo_candidato.lastNames, 'mail':nuevo_candidato.mail}, 201
    
    def get(self):
        mail = request.args.get('mail', default = "none", type=str)
        try:
                return[candidato_schema.dump(t) for t in Candidato.query.filter(
                (Candidato.mail == mail) | (mail == 'none'))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412


# Candidatos
# Vista PATCH - GET
class VistaCandidato(Resource):
    def patch(self, id):
        
        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            candidato = Candidato.query.get(id)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404
            else:
                if "names" in request.json:
                    if request.json["names"] == "":
                        return 'El campo names es requerido', 400

                    candidato.names = request.json["names"]

                if "lastNames" in request.json:
                    if request.json["lastNames"] == "":
                        return 'El campo lastNames es requerido', 400
                    candidato.lastNames = request.json["lastNames"]

                if "mail" in request.json:
                    if request.json["mail"] == "":
                        return 'El campo mail es requerido', 400
                    candidato.mail = request.json["mail"]

                if "docType" in request.json:
                    if request.json["docType"] == "":
                        db.session.rollback()
                        return 'El campo docType es requerido', 400
                    candidato.docType = request.json["docType"]

                if "phone" in request.json:
                    if request.json["phone"] == "":
                        db.session.rollback()
                        return 'El campo phone es requerido', 400
                    candidato.phone = request.json["phone"]

                if "address" in request.json:
                    if request.json["address"] == "":
                        db.session.rollback()
                        return 'El campo address es requerido', 400
                    

                    candidato.lastNamess = request.json["address"]

                if "birthDate" in request.json:
                    if request.json["birthDate"] == "":
                        db.session.rollback()
                        return 'El campo birthDate es requerido', 400
                    try:
                        birthDate = datetime.strptime(request.json["birthDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
                    except:
                        db.session.rollback()
                        return "El campo birthDate no tiene formato de fecha correcto", 400
                    candidato.birthDate = birthDate

                if "country" in request.json:
                    if request.json["country"] == "":
                        db.session.rollback()
                        return 'El campo country es requerido', 400
                    candidato.country = request.json["country"]


                if "country" in request.json:
                    if request.json["language"] == "":
                        db.session.rollback()
                        return 'El campo language es requerido', 400
                    candidato.country = request.json["language"]

                if "city" in request.json:
                    if request.json["city"] == "":
                        db.session.rollback()
                        return 'El campo city es requerido', 400
                    candidato.city = request.json["city"]
                try:
                    db.session.commit()
                    return candidato_schema.dump(candidato), 200
                except:
                    db.session.rollback()
                    return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, id):
        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            candidato = Candidato.query.get(id)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404
            else:
                return candidato_schema.dump(candidato)
            
# PING
# Vista GET
class VistaPing(Resource):
    def get(self):
        return "pong"            

# Informacion Academica
# Vista POST - GET

class VistaInformacionesAcademicas(Resource):
    def post(self, candidatoId):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(id)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404
        if not "tittle" in request.json or not "institution" in request.json or not "beginDate" in request.json or not "studyType" in request.json:
            return 'Los campos tittle, institution, beginDate, studyType', 400
        if request.json["tittle"] == "" or request.json["institution"] == "" or request.json["tipoEstudio"] == "": 
            return 'Los campos tittle, institution, studyType son requeridos', 400
        try:
            beginDate = datetime.strptime(request.json["beginDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            return "El campo beginDate no tiene formato de fecha correcto", 400


        if "endDate" in request.json:
            try:
                endDate = datetime.strptime(request.json["endDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
            except:
                return "El campo endDate no tiene formato de fecha correcto", 400
        else:
            endDate = None

        try:
            nueva_informacion = InformacionAcademica(tittle=request.json["tittle"], 
                                        institution=request.json["institution"],
                                        beginDate=beginDate,
                                        endDate=endDate,
                                        studyType=request.json["studyType"],
                                        candidatoId=candidatoId)
            db.session.add(nueva_informacion)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        return informacion_schema.dump(nueva_informacion), 201
    
    def get(self, candidatoId):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(id)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404
            
        try:
                return[informacion_schema.dump(t) for t in InformacionAcademica.query.filter(
                (InformacionAcademica.candidatoId == candidatoId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        
# Informacion Academica
# Vista PATCH - GET - DELETE
class VistaInformacionAcademica(Resource):

    def patch(self, candidatoId, id):
        
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            informacionAcademica = InformacionAcademica.query.get(id)
            if informacionAcademica is None:
                return 'No existe la Información Académica del candidato solicitada', 404


            if "tittle" in request.json:
                if request.json["tittle"] == "":
                    return 'El campo tittle es requerido', 400
                informacionAcademica.tittle = request.json["tittle"]

            if "institution" in request.json:
                if request.json["institution"] == "":
                    return 'El campo institution es requerido', 400
                informacionAcademica.institution = request.json["institution"]

            if "beginDate" in request.json:
                if request.json["beginDate"] == "":
                    db.session.rollback()
                    return 'El campo beginDate es requerido', 400
                try:
                    beginDate = datetime.strptime(request.json["beginDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
                except:
                    db.session.rollback()
                    return "El campo beginDate no tiene formato de fecha correcto", 400
                informacionAcademica.beginDate = beginDate

            endDate = None
            if "endDate" in request.json:
                if request.json["endDate"] == "" or request.json["endDate"] == None:
                    endDate = None
                try:
                    endDate = datetime.strptime(request.json["endDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
                except:
                    db.session.rollback()
                    return "El campo endDate no tiene formato de fecha correcto", 400
                informacionAcademica.endDate = endDate

            if "studyType" in request.json:
                if request.json["studyType"] == "":
                    db.session.rollback()
                    return 'El campo studyType es requerido', 400
                informacionAcademica.studyType = request.json["studyType"]

            try:
                db.session.commit()
                return informacion_schema.dump(informacionAcademica), 200
            except:
                db.session.rollback()
                return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, candidatoId, id):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            informacionAcademica = InformacionAcademica.query.get(id)
            if informacionAcademica is None:
                return 'No existe la Información Académica del candidato solicitada', 404
        return informacion_schema.dump(informacionAcademica), 200

    def delete(self, candidatoId, id):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            informacionAcademica = InformacionAcademica.query.get(id)
            if informacionAcademica is None:
                return 'No existe la Información Académica del candidato solicitada', 404
        try:
            informacionAcademica.delete()
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        



# Informacion Tecnica
# Vista POST - GET
class VistaInformacionesTecnicas(Resource):
    def post(self, candidatoId):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(id)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404
            
        if not "type" in request.json or not "description" in request.json:
            return 'Los campos type, description son requeridos', 400
        if request.json["type"] == "" or request.json["description"] == "": 
            return 'Los campos type, description, studyType son requeridos', 400

        try:
            nueva_informacion = InformacionTecnica(type=request.json["type"], 
                                        description=request.json["description"],
                                        candidatoId=candidatoId)
            db.session.add(nueva_informacion)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        return informacionTecnica_schema.dump(nueva_informacion), 201
    
    def get(self, candidatoId):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(id)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404
            
        try:
                return[informacionTecnica_schema.dump(t) for t in InformacionTecnica.query.filter(
                (InformacionTecnica.candidatoId == candidatoId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        
# Informacion Tecnica
# Vista PATCH - GET - DELETE
class VistaInformacionTecnica(Resource):

    def patch(self, candidatoId, id):
        
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            informacionTecnica = InformacionTecnica.query.get(id)
            if informacionTecnica is None:
                return 'No existe la Información Técnica del candidato solicitada', 404


            if "type" in request.json:
                if request.json["type"] == "":
                    return 'El campo type es requerido', 400
                informacionTecnica.tittle = request.json["type"]

            if "description" in request.json:
                if request.json["description"] == "":
                    return 'El campo description es requerido', 400
                informacionTecnica.institution = request.json["description"]

            try:
                db.session.commit()
                return informacion_schema.dump(informacionTecnica), 200
            except:
                db.session.rollback()
                return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, candidatoId, id):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            informacionTecnica = InformacionTecnica.query.get(id)
            if informacionTecnica is None:
                return 'No existe la Información Técnica del candidato solicitada', 404
        return informacionTecnica_schema.dump(informacionTecnica), 200


    def delete(self, candidatoId, id):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            informacionTecnica = InformacionAcademica.query.get(id)
            if informacionTecnica is None:
                return 'No existe la Información Técnica del candidato solicitada', 404
        try:
            informacionTecnica.delete()
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412


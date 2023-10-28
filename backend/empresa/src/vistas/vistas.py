from flask_restful import Resource
from flask import request
from ..modelos import db, Empresa, EmpresaEschema
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys

empresa_schema = EmpresaEschema()
# informacion_schema = InformacionAcademicaEschema()
# informacionTecnica_schema = InformacionTecnicaEschema()
# informacionLaboral_schema = InformacionLaboralEschema()


# Empresas
# Vista POST - GET
class VistaRegistro(Resource):

    def post(self):
        if not "name" in request.json or not "mail" in request.json or not "password" in request.json or not "confirmPassword" in request.json:
            return 'Los campos name, mail, password y confirmPassword son requeridos', 400

        if request.json["name"] == "" or request.json["mail"] == ""  or request.json["password"] == ""  or request.json["confirmPassword"] == "" : 
            return 'Los campos name, mail, password y confirmPassword son requeridos', 400

        if request.json["password"] != request.json["confirmPassword"]: 
            return 'El campo password y el campo confirmPassword deben ser requeridos', 409

        try:
            nuevo_empresa = Empresa(name=request.json["name"], 
                                        mail=request.json["mail"],
                                        password=request.json["password"])

            db.session.add(nuevo_empresa)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return {'id':nuevo_empresa.id, 'name': nuevo_empresa.name, 'mail':nuevo_empresa.mail}, 201
    
    def get(self):
        mail = request.args.get('mail', default = "none", type=str)
        try:
                return[empresa_schema.dump(t) for t in Empresa.query.filter(
                (Empresa.mail == mail) | (mail == 'none'))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412


# Empresas
# Vista PATCH - GET
# class VistaEmpresa(Resource):
#     def patch(self, id):
        
#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             empresa = Empresa.query.get(id)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404
#             else:
#                 if "name" in request.json:
#                     if request.json["name"] == "":
#                         return 'El campo name es requerido', 400

#                     empresa.name = request.json["name"]

#                 if "mail" in request.json:
#                     if request.json["mail"] == "":
#                         return 'El campo mail es requerido', 400
#                     empresa.mail = request.json["mail"]

#                 if "docType" in request.json:
#                     if request.json["docType"] == "":
#                         db.session.rollback()
#                         return 'El campo docType es requerido', 400
#                     empresa.docType = request.json["docType"]

#                 if "docNumber" in request.json:
#                     if request.json["docNumber"] == "":
#                         db.session.rollback()
#                         return 'El campo docNumber es requerido', 400
#                     empresa.docNumber = request.json["docNumber"]

#                 if "phone" in request.json:
#                     if request.json["phone"] == "":
#                         db.session.rollback()
#                         return 'El campo phone es requerido', 400
#                     empresa.phone = request.json["phone"]

#                 if "address" in request.json:
#                     if request.json["address"] == "":
#                         db.session.rollback()
#                         return 'El campo address es requerido', 400                    
#                     empresa.address = request.json["address"]

#                 if "birthDate" in request.json:
#                     if request.json["birthDate"] == "":
#                         db.session.rollback()
#                         return 'El campo birthDate es requerido', 400
#                     try:
#                         birthDate = datetime.strptime(request.json["birthDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
#                     except:
#                         db.session.rollback()
#                         return "El campo birthDate no tiene formato de fecha correcto", 400
#                     empresa.birthDate = birthDate

#                 if "country" in request.json:
#                     if request.json["country"] == "":
#                         db.session.rollback()
#                         return 'El campo country es requerido', 400
#                     empresa.country = request.json["country"]


#                 if "language" in request.json:
#                     if request.json["language"] == "":
#                         db.session.rollback()
#                         return 'El campo language es requerido', 400
#                     empresa.language = request.json["language"]

#                 if "city" in request.json:
#                     if request.json["city"] == "":
#                         db.session.rollback()
#                         return 'El campo city es requerido', 400
#                     empresa.city = request.json["city"]
                    
#                 try:
#                     db.session.commit()
#                     return empresa_schema.dump(empresa), 200
#                 except:
#                     db.session.rollback()
#                     return {'Error': str(sys.exc_info()[0])}, 412
                
#     def get(self, id):
#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             empresa = Empresa.query.get(id)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404
#             else:
#                 return empresa_schema.dump(empresa), 200
            
# PING
# Vista GET
class VistaPing(Resource):
    def get(self):
        return "pong"            

# # Informacion Academica
# # Vista POST - GET

# class VistaInformacionesAcademicas(Resource):
#     def post(self, empresaId):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404
#         if not "title" in request.json or not "institution" in request.json or not "beginDate" in request.json or not "studyType" in request.json:
#             return 'Los campos title, institution, beginDate, studyType', 400
#         if request.json["title"] == "" or request.json["institution"] == "" or request.json["studyType"] == "": 
#             return 'Los campos title, institution, studyType son requeridos', 400
#         try:
#             beginDate = datetime.strptime(request.json["beginDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
#         except:
#             return "El campo beginDate no tiene formato de fecha correcto", 400


#         if "endDate" in request.json:
#             try:
#                 endDate = datetime.strptime(request.json["endDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
#             except:
#                 return "El campo endDate no tiene formato de fecha correcto", 400
#         else:
#             endDate = None

#         try:
#             nueva_informacion = InformacionAcademica(title=request.json["title"], 
#                                         institution=request.json["institution"],
#                                         beginDate=beginDate,
#                                         endDate=endDate,
#                                         empresaId=empresaId,
#                                         studyType=request.json["studyType"])
#             db.session.add(nueva_informacion)
#             db.session.commit()
#         except:
#             db.session.rollback()
#             return {'Error': str(sys.exc_info()[0])}, 412
        
#         return informacion_schema.dump(nueva_informacion), 201


    
#     def get(self, empresaId):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404
            
#         try:
#                 return[informacion_schema.dump(t) for t in InformacionAcademica.query.filter(
#                 (InformacionAcademica.empresaId == empresaId))], 200
#         except:
#             return {'Error': str(sys.exc_info()[0])}, 412
        
# # Informacion Academica
# # Vista PATCH - GET - DELETE
# class VistaInformacionAcademica(Resource):

#     def patch(self, empresaId, id):
        
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404

#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             informacionAcademica = InformacionAcademica.query.get(id)
#             if informacionAcademica is None:
#                 return 'No existe la Información Académica del empresa solicitada', 404


#             if "title" in request.json:
#                 if request.json["title"] == "":
#                     return 'El campo title es requerido', 400
#                 informacionAcademica.title = request.json["title"]

#             if "institution" in request.json:
#                 if request.json["institution"] == "":
#                     return 'El campo institution es requerido', 400
#                 informacionAcademica.institution = request.json["institution"]

#             if "beginDate" in request.json:
#                 if request.json["beginDate"] == "":
#                     db.session.rollback()
#                     return 'El campo beginDate es requerido', 400
#                 try:
#                     beginDate = datetime.strptime(request.json["beginDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
#                 except:
#                     db.session.rollback()
#                     return "El campo beginDate no tiene formato de fecha correcto", 400
#                 informacionAcademica.beginDate = beginDate

#             if "endDate" in request.json:
#                 if request.json["endDate"] == "" or request.json["endDate"] == None:
#                     endDate = None
#                 else:
#                     try:
#                         endDate = datetime.strptime(request.json["endDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
#                     except:
#                         db.session.rollback()
#                         return "El campo endDate no tiene formato de fecha correcto", 400
#                 informacionAcademica.endDate = endDate

#             if "studyType" in request.json:
#                 if request.json["studyType"] == "":
#                     db.session.rollback()
#                     return 'El campo studyType es requerido', 400
#                 informacionAcademica.studyType = request.json["studyType"]

#             try:
#                 db.session.commit()
#                 return informacion_schema.dump(informacionAcademica), 200
#             except:
#                 db.session.rollback()
#                 return {'Error': str(sys.exc_info()[0])}, 412
                
#     def get(self, empresaId, id):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404

#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             informacionAcademica = InformacionAcademica.query.get(id)
#             if informacionAcademica is None:
#                 return 'No existe la Información Académica del empresa solicitada', 404
#         return informacion_schema.dump(informacionAcademica), 200

#     def delete(self, empresaId, id):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404

#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             informacionAcademica = InformacionAcademica.query.get(id)
#             if informacionAcademica is None:
#                 return 'No existe la Información Académica del empresa solicitada', 404
#         try:
#             db.session.delete(informacionAcademica)
#             db.session.commit()
#             return 'Registro Eliminado Correctamente', 204
#         except:
#             db.session.rollback()
#             return {'Error': str(sys.exc_info()[0])}, 412
        



# # Informacion Tecnica
# # Vista POST - GET
# class VistaInformacionesTecnicas(Resource):
#     def post(self, empresaId):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404
            
#         if not "type" in request.json or not "description" in request.json:
#             return 'Los campos type, description son requeridos', 400
#         if request.json["type"] == "" or request.json["description"] == "": 
#             return 'Los campos type, description, studyType son requeridos', 400

#         try:
#             nueva_informacion = InformacionTecnica(type=request.json["type"], 
#                                         description=request.json["description"],
#                                         empresaId=empresaId)
#             db.session.add(nueva_informacion)
#             db.session.commit()
#         except:
#             db.session.rollback()
#             return {'Error': str(sys.exc_info()[0])}, 412
#         return informacionTecnica_schema.dump(nueva_informacion), 201
    
#     def get(self, empresaId):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404
            
#         try:
#                 return[informacionTecnica_schema.dump(t) for t in InformacionTecnica.query.filter(
#                 (InformacionTecnica.empresaId == empresaId))], 200
#         except:
#             return {'Error': str(sys.exc_info()[0])}, 412
        
# # Informacion Tecnica
# # Vista PATCH - GET - DELETE
# class VistaInformacionTecnica(Resource):

#     def patch(self, empresaId, id):
        
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404

#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             informacionTecnica = InformacionTecnica.query.get(id)
#             if informacionTecnica is None:
#                 return 'No existe la Información Técnica del empresa solicitada', 404


#             if "type" in request.json:
#                 if request.json["type"] == "":
#                     return 'El campo type es requerido', 400
#                 informacionTecnica.type = request.json["type"]

#             if "description" in request.json:
#                 if request.json["description"] == "":
#                     return 'El campo description es requerido', 400
#                 informacionTecnica.description = request.json["description"]

#             try:
#                 db.session.commit()
#                 return informacionTecnica_schema.dump(informacionTecnica), 200
#             except:
#                 db.session.rollback()
#                 return {'Error': str(sys.exc_info()[0])}, 412
                
#     def get(self, empresaId, id):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404

#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             informacionTecnica = InformacionTecnica.query.get(id)
#             if informacionTecnica is None:
#                 return 'No existe la Información Técnica del empresa solicitada', 404
#         return informacionTecnica_schema.dump(informacionTecnica), 200


#     def delete(self, empresaId, id):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404

#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             informacionTecnica = InformacionTecnica.query.get(id)
#             if informacionTecnica is None:
#                 return 'No existe la Información Técnica del empresa solicitada', 404
#         try:
#             db.session.delete(informacionTecnica)
#             db.session.commit()
#             return 'Registro Eliminado Correctamente', 204
#         except:
#             db.session.rollback()
#             return {'Error': str(sys.exc_info()[0])}, 412



# # Informacion Laboral
# # Vista POST - GET
# class VistaInformacionesLaborales(Resource):
#     def post(self, empresaId):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404
            
#         if not "position" in request.json or not "organization" in request.json or not "activities" in request.json  or not "dateFrom" in request.json:
#             return 'Los campos position, organization, activities y dateFrom son requeridos', 400
#         if request.json["position"] == "" or request.json["organization"] == "" or request.json["activities"] == "": 
#             return 'Los campos position, organization, activities y dateFrom son requeridos', 400

#         try:
#             dateFrom = datetime.strptime(request.json["dateFrom"], "%Y-%m-%dT%H:%M:%S.%fZ")
#         except:
#             return "El campo dateFrom no tiene formato de fecha correcto", 400

#         dateTo = None
#         if "dateTo" in request.json:
#             if request.json["dateTo"] != None:
#                 try:
#                     dateTo = datetime.strptime(request.json["dateTo"], "%Y-%m-%dT%H:%M:%S.%fZ")
#                 except:
#                     return "El campo dateTo no tiene formato de fecha correcto", 400
                
        
                





#         try:
#             nueva_informacion = InformacionLaboral(position=request.json["position"], 
#                                         organization=request.json["organization"],
#                                         activities=request.json["activities"],
#                                         dateFrom=dateFrom,
#                                         dateTo=dateTo,
#                                         empresaId=empresaId)
#             db.session.add(nueva_informacion)
#             db.session.commit()
#         except:
#             db.session.rollback()
#             return {'Error': str(sys.exc_info()[0])}, 412
#         return informacionLaboral_schema.dump(nueva_informacion), 201
    
#     def get(self, empresaId):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404
            
#         try:
#                 return[informacionLaboral_schema.dump(t) for t in InformacionLaboral.query.filter(
#                 (InformacionLaboral.empresaId == empresaId))], 200
#         except:
#             return {'Error': str(sys.exc_info()[0])}, 412
        
# # Informacion Laboral
# # Vista PATCH - GET - DELETE
# class VistaInformacionLaboral(Resource):

#     def patch(self, empresaId, id):
        
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404

#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             informacionLaboral = InformacionLaboral.query.get(id)
#             if informacionLaboral is None:
#                 return 'No existe la Información Laboral del empresa solicitada', 404


#             if "position" in request.json:
#                 if request.json["position"] == "":
#                     return 'El campo position es requerido', 400
#                 informacionLaboral.position = request.json["position"]

#             if "organization" in request.json:
#                 if request.json["organization"] == "":
#                     return 'El campo organization es requerido', 400
#                 informacionLaboral.organization = request.json["organization"]

#             if "activities" in request.json:
#                 if request.json["activities"] == "":
#                     return 'El campo activities es requerido', 400
#                 informacionLaboral.activities = request.json["activities"]


#             if "dateFrom" in request.json:
#                 if request.json["dateFrom"] == "":
#                     return 'El campo dateFrom es requerido', 400
#                 try:
#                     dateFrom = datetime.strptime(request.json["dateFrom"], "%Y-%m-%dT%H:%M:%S.%fZ")
#                 except:
#                     return "El campo dateFrom no tiene formato de fecha correcto", 400

#                 informacionLaboral.dateFrom = dateFrom

#             dateTo = None
#             if "dateTo" in request.json:
#                 if request.json["dateTo"] != "" and request.json["dateTo"] != None :
#                     try:
#                         dateTo = datetime.strptime(request.json["dateTo"], "%Y-%m-%dT%H:%M:%S.%fZ")
#                     except:
#                         return "El campo dateTo no tiene formato de fecha correcto", 400
#                 informacionLaboral.dateTo = dateTo

#             try:
#                 db.session.commit()
#                 return informacionLaboral_schema.dump(informacionLaboral), 200
#             except:
#                 db.session.rollback()
#                 return {'Error': str(sys.exc_info()[0])}, 412
                
#     def get(self, empresaId, id):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404

#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             informacionLaboral = InformacionLaboral.query.get(id)
#             if informacionLaboral is None:
#                 return 'No existe la Información Laboral del empresa solicitada', 404
#         return informacionLaboral_schema.dump(informacionLaboral), 200


#     def delete(self, empresaId, id):
#         if empresaId.isnumeric() == False:
#             return 'El empresaId no es un número.', 400
#         else:
#             empresa = Empresa.query.get(empresaId)
#             if empresa is None:
#                 return 'No existe la cuenta del empresa solicitada', 404

#         if id.isnumeric() == False:
#             return 'El id no es un número.', 400
#         else:
#             informacionLaboral = InformacionLaboral.query.get(id)
#             if informacionLaboral is None:
#                 return 'No existe la Información Laboral del empresa solicitada', 404
#         try:
#             db.session.delete(informacionLaboral)
#             db.session.commit()
#             return 'Registro Eliminado Correctamente', 204
#         except:
#             db.session.rollback()
#             return {'Error': str(sys.exc_info()[0])}, 412

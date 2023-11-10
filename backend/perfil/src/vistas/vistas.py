from flask_restful import Resource
from flask import request
from ..modelos import db, Perfil, PerfilEschema, Habilidad, HabilidadEschema, Conocimiento, ConocimientoEschema, Idioma, IdiomaEschema
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys, os

perfil_schema = PerfilEschema()
habilidad_schema = HabilidadEschema()
conocimiento_schema = ConocimientoEschema()
idioma_schema = IdiomaEschema()


# Perfiles
# Vista POST - GET
class VistaPerfiles(Resource):

    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def post(self,empresaId,proyectoId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if not "name" in request.json or not "role" in request.json or not "location" in request.json or not "years" in request.json:
            return 'Los campos name, role, location, years y confirmYears son requeridos', 400

        if request.json["name"] == "" or request.json["role"] == ""  or request.json["location"] == ""  or request.json["years"] == "": 
            return 'Los campos name, role, location y years son requeridos', 400

        try:
            nuevo_perfil = Perfil(name=request.json["name"], 
                                        role=request.json["role"],
                                        location=request.json["location"],
                                        years=request.json["years"],
                                        proyectoId=proyectoId)

            db.session.add(nuevo_perfil)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return {'id':nuevo_perfil.id, 'name': nuevo_perfil.name, 'role': nuevo_perfil.role, 'location':nuevo_perfil.location, 'years':nuevo_perfil.years, 'proyectoId':nuevo_perfil.proyectoId}, 201
    
    def get(self,empresaId,proyectoId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 
            
        try:
                return[perfil_schema.dump(t) for t in Perfil.query.filter(
                Perfil.proyectoId == proyectoId)], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412


# Perfiles
# Vista PATCH - GET - DELETE
class VistaPerfil(Resource):

    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def patch(self, empresaId, proyectoId, id):


        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 
            
        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            perfil = Perfil.query.get(id)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404
            else:
                if "name" in request.json:
                    if request.json["name"] == "":
                        return 'El campo name es requerido', 400

                    perfil.name = request.json["name"]

                if "role" in request.json:
                    if request.json["role"] == "":
                        return 'El campo role es requerido', 400
                    perfil.role = request.json["role"]

                if "location" in request.json:
                    if request.json["location"] == "":
                        return 'El campo location es requerido', 400
                    perfil.location = request.json["location"]

                if "years" in request.json:
                    if request.json["years"] == "":
                        db.session.rollback()
                        return 'El campo years es requerido', 400
                    perfil.years = request.json["years"]
                    
                try:
                    db.session.commit()
                    return perfil_schema.dump(perfil), 200
                except:
                    db.session.rollback()
                    return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, empresaId, proyectoId, id):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            perfil = Perfil.query.get(id)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404
            else:
                return perfil_schema.dump(perfil), 200
            

    def delete(self, empresaId, proyectoId, id):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            perfil = Perfil.query.get(id)
            if perfil is None:
                return 'No existe el perfil solicitado', 404
        try:
            db.session.delete(perfil)
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

# Habilidad
# Vista POST - GET

class VistaHabilidades(Resource):
    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def post(self, empresaId, proyectoId, perfilId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 


        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if not "name" in request.json or not "description" in request.json:
            return 'Los campos name, description son requeridos', 400
        if request.json["name"] == "" or request.json["description"] == "": 
            return 'Los campos name, description son requeridos', 400

        try:
            nueva_habilidad = Habilidad(name=request.json["name"], 
                                        description=request.json["description"],
                                        perfilId=perfilId)
            db.session.add(nueva_habilidad)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return habilidad_schema.dump(nueva_habilidad), 201
    
    def get(self, empresaId, proyectoId, perfilId):


        if empresaId.isnumeric() == False:
            return 'El id de la empresa no es un número.', 400
        if proyectoId.isnumeric() == False:
            return 'El id del proyecto no es un número.', 400
        else:
            response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
            if response.status_code != 200:
                return response.text, response.status_code 

        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404
            
        try:
                return[habilidad_schema.dump(t) for t in Habilidad.query.filter(
                (Habilidad.perfilId == perfilId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        

        
# Habilidad
# Vista PATCH - GET - DELETE
class VistaHabilidad(Resource):
    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def patch(self, empresaId, proyectoId, perfilId, id):
        

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 



        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            habilidad = Habilidad.query.get(id)
            if habilidad is None:
                return 'No existe la Habilidad del perfil solicitada', 404


            if "name" in request.json:
                if request.json["name"] == "":
                    return 'El campo name es requerido', 400
                habilidad.name = request.json["name"]

            if "description" in request.json:
                if request.json["description"] == "":
                    return 'El campo description es requerido', 400
                habilidad.description = request.json["description"]

            if "beginDate" in request.json:
                if request.json["beginDate"] == "":
                    db.session.rollback()
                    return 'El campo beginDate es requerido', 400
                try:
                    beginDate = datetime.strptime(request.json["beginDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
                except:
                    db.session.rollback()
                    return "El campo beginDate no tiene formato de fecha correcto", 400
                habilidad.beginDate = beginDate

            try:
                db.session.commit()
                return habilidad_schema.dump(habilidad), 200
            except:
                db.session.rollback()
                return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, empresaId, proyectoId, perfilId, id):


        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            habilidad = Habilidad.query.get(id)
            if habilidad is None:
                return 'No existe la Habilidad del perfil solicitada', 404
        return habilidad_schema.dump(habilidad), 200

    def delete(self, empresaId, proyectoId, perfilId, id):


        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 


        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            habilidad = Habilidad.query.get(id)
            if habilidad is None:
                return 'No existe la Habilidad del perfil solicitada', 404
        try:
            db.session.delete(habilidad)
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
# Conocimiento
# Vista POST - GET

class VistaConocimientos(Resource):

    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def post(self, empresaId, proyectoId, perfilId):


        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if not "name" in request.json or not "description" in request.json:
            return 'Los campos name, description son requeridos', 400
        if request.json["name"] == "" or request.json["description"] == "": 
            return 'Los campos name, description son requeridos', 400

        try:
            nueva_conocimiento = Conocimiento(name=request.json["name"], 
                                        description=request.json["description"],
                                        perfilId=perfilId)
            db.session.add(nueva_conocimiento)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return conocimiento_schema.dump(nueva_conocimiento), 201
    
    def get(self, empresaId, proyectoId, perfilId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404
            
        try:
                return[conocimiento_schema.dump(t) for t in Conocimiento.query.filter(
                (Conocimiento.perfilId == perfilId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        

        
# Conocimiento
# Vista PATCH - GET - DELETE
class VistaConocimiento(Resource):
    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def patch(self, empresaId, proyectoId, perfilId, id):
    
        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            conocimiento = Conocimiento.query.get(id)
            if conocimiento is None:
                return 'No existe la Conocimiento del perfil solicitada', 404


            if "name" in request.json:
                if request.json["name"] == "":
                    return 'El campo name es requerido', 400
                conocimiento.name = request.json["name"]

            if "description" in request.json:
                if request.json["description"] == "":
                    return 'El campo description es requerido', 400
                conocimiento.description = request.json["description"]

            if "beginDate" in request.json:
                if request.json["beginDate"] == "":
                    db.session.rollback()
                    return 'El campo beginDate es requerido', 400
                try:
                    beginDate = datetime.strptime(request.json["beginDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
                except:
                    db.session.rollback()
                    return "El campo beginDate no tiene formato de fecha correcto", 400
                conocimiento.beginDate = beginDate

            try:
                db.session.commit()
                return conocimiento_schema.dump(conocimiento), 200
            except:
                db.session.rollback()
                return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, empresaId, proyectoId, perfilId, id):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            conocimiento = Conocimiento.query.get(id)
            if conocimiento is None:
                return 'No existe la Conocimiento del perfil solicitada', 404
        return conocimiento_schema.dump(conocimiento), 200

    def delete(self, empresaId, proyectoId, perfilId, id):


        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 


        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            conocimiento = Conocimiento.query.get(id)
            if conocimiento is None:
                return 'No existe la Conocimiento del perfil solicitada', 404
        try:
            db.session.delete(conocimiento)
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412

# Idioma
# Vista POST - GET

class VistaIdiomas(Resource):
    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def post(self, empresaId, proyectoId, perfilId):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 


        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if not "name" in request.json or not "description" in request.json:
            return 'Los campos name, description son requeridos', 400
        if request.json["name"] == "" or request.json["description"] == "": 
            return 'Los campos name, description son requeridos', 400

        try:
            nueva_idioma = Idioma(name=request.json["name"], 
                                        description=request.json["description"],
                                        perfilId=perfilId)
            db.session.add(nueva_idioma)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return idioma_schema.dump(nueva_idioma), 201
    
    def get(self, empresaId, proyectoId, perfilId):


        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404
            
        try:
                return[idioma_schema.dump(t) for t in Idioma.query.filter(
                (Idioma.perfilId == perfilId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        

        
# Idioma
# Vista PATCH - GET - DELETE
class VistaIdioma(Resource):
    def __init__(self, **kwargs):
        self.urlBackEnd = str(os.getenv("EMPR_BACK_URL")) + "/empresa"

    def patch(self, empresaId, proyectoId, perfilId, id):
        
        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 



        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            idioma = Idioma.query.get(id)
            if idioma is None:
                return 'No existe la Idioma del perfil solicitada', 404


            if "name" in request.json:
                if request.json["name"] == "":
                    return 'El campo name es requerido', 400
                idioma.name = request.json["name"]

            if "description" in request.json:
                if request.json["description"] == "":
                    return 'El campo description es requerido', 400
                idioma.description = request.json["description"]

            if "beginDate" in request.json:
                if request.json["beginDate"] == "":
                    db.session.rollback()
                    return 'El campo beginDate es requerido', 400
                try:
                    beginDate = datetime.strptime(request.json["beginDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
                except:
                    db.session.rollback()
                    return "El campo beginDate no tiene formato de fecha correcto", 400
                idioma.beginDate = beginDate

            try:
                db.session.commit()
                return idioma_schema.dump(idioma), 200
            except:
                db.session.rollback()
                return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, empresaId, proyectoId, perfilId, id):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 

        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            idioma = Idioma.query.get(id)
            if idioma is None:
                return 'No existe la Idioma del perfil solicitada', 404
        return idioma_schema.dump(idioma), 200

    def delete(self, empresaId, proyectoId, perfilId, id):

        response = requests.get(self.urlBackEnd + "/" + empresaId + "/proyecto/" + proyectoId)
        if response.status_code != 200:
            return response.text, response.status_code 


        if perfilId.isnumeric() == False:
            return 'El perfilId no es un número.', 400
        else:
            perfil = Perfil.query.get(perfilId)
            if perfil is None:
                return 'No existe la cuenta del perfil solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            idioma = Idioma.query.get(id)
            if idioma is None:
                return 'No existe la Idioma del perfil solicitada', 404
        try:
            db.session.delete(idioma)
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412

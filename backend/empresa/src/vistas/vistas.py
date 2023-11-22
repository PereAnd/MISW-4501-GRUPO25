from flask_restful import Resource
from flask import request
from ..modelos import db, Empresa, EmpresaEschema, Vertical, VerticalEschema, Ubicacion, UbicacionEschema, Proyecto, ProyectoEschema, Entrevista, EntrevistaEschema, Aplicacion, AplicacionEschema
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys

empresa_schema = EmpresaEschema()
vertical_schema = VerticalEschema()
entrevista_schema = EntrevistaEschema()
ubicacion_schema = UbicacionEschema()
proyecto_schema = ProyectoEschema()
aplicacion_schema = AplicacionEschema()
# informacion_schema = InformacionAcademicaEschema()
# informacionTecnica_schema = InformacionTecnicaEschema()
# informacionLaboral_schema = InformacionLaboralEschema()


# Empresas

class VistaLogIn(Resource):
    def post(self):
        if not "mail" in request.json or not "password" in request.json:
            return 'Los campos mail y password son requeridos', 400

        if request.json["mail"] == "" or request.json["password"] == "":
            return 'Los campos mail y password son requeridos', 400

        empresa = Empresa.query.filter_by(mail=request.json["mail"]).first()

        if empresa and empresa.password == request.json["password"]:
            return {'id_empresa': empresa.id}, 200
        else:
            return 'Mail o contraseña incorrecta', 401


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
class VistaEmpresa(Resource):
    def patch(self, id):
        
        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            empresa = Empresa.query.get(id)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404
            else:
                if "name" in request.json:
                    if request.json["name"] == "":
                        return 'El campo name es requerido', 400

                    empresa.name = request.json["name"]

                if "mail" in request.json:
                    if request.json["mail"] == "":
                        return 'El campo mail es requerido', 400
                    empresa.mail = request.json["mail"]

                if "docType" in request.json:
                    if request.json["docType"] == "":
                        db.session.rollback()
                        return 'El campo docType es requerido', 400
                    empresa.docType = request.json["docType"]

                if "docNumber" in request.json:
                    if request.json["docNumber"] == "":
                        db.session.rollback()
                        return 'El campo docNumber es requerido', 400
                    empresa.docNumber = request.json["docNumber"]

                if "organizationType" in request.json:
                    if request.json["organizationType"] == "":
                        db.session.rollback()
                        return 'El campo organizationType es requerido', 400                    
                    empresa.organizationType = request.json["organizationType"]

                if "description" in request.json:
                    if request.json["description"] == "":
                        db.session.rollback()
                        return 'El campo description es requerido', 400                    
                    empresa.description = request.json["description"]
                   
                try:
                    db.session.commit()
                    return empresa_schema.dump(empresa), 200
                except:
                    db.session.rollback()
                    return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, id):
        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            empresa = Empresa.query.get(id)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404
            else:
                return empresa_schema.dump(empresa), 200
            
# PING
# Vista GET
class VistaPing(Resource):
    def get(self):
        return "pong"            


# Vertical
# Vista POST - GET

class VistaVerticales(Resource):
    def post(self, empresaId):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404
        if not "vertical" in request.json or not "description" in request.json:
            return 'Los campos vertical, description son requeridos', 400
        if request.json["vertical"] == "" or request.json["description"] == "": 
            return 'Los campos vertical, description son requeridos', 400


        try:
            nueva_vertical = Vertical(vertical=request.json["vertical"], 
                                        description=request.json["description"], empresaId=empresaId)
            db.session.add(nueva_vertical)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return vertical_schema.dump(nueva_vertical), 201


    
    def get(self, empresaId):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404
            
        try:
                return[vertical_schema.dump(t) for t in Vertical.query.filter(
                (Vertical.empresaId == empresaId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        
# Vertical
# Vista PATCH - GET - DELETE
class VistaVertical(Resource):

    def patch(self, empresaId, id):
        
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            vertical = Vertical.query.get(id)
            if vertical is None:
                return 'No existe la Vertical del empresa solicitada', 404


            if "vertical" in request.json:
                if request.json["vertical"] == "":
                    return 'El campo vertical es requerido', 400
                vertical.vertical = request.json["vertical"]

            if "description" in request.json:
                if request.json["description"] == "":
                    return 'El campo description es requerido', 400
                vertical.description = request.json["description"]

            try:
                db.session.commit()
                return vertical_schema.dump(vertical), 200
            except:
                db.session.rollback()
                return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, empresaId, id):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            vertical = Vertical.query.get(id)
            if vertical is None:
                return 'No existe la Vertical del empresa solicitada', 404
        return vertical_schema.dump(vertical), 200

    def delete(self, empresaId, id):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            vertical = Vertical.query.get(id)
            if vertical is None:
                return 'No existe la Vertical del empresa solicitada', 404
        try:
            db.session.delete(vertical)
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412




# Ubicacion
# Vista POST - GET

class VistaUbicaciones(Resource):
    def post(self, empresaId):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404
        if not "country" in request.json or not "city" in request.json or not "description" in request.json:
            return 'Los campos country, city, description son requeridos', 400
        if request.json["country"] == "" or request.json["city"] == "" or request.json["description"] == "": 
            return 'Los campos country, city, description son requeridos', 400


        try:
            nueva_ubicacion = Ubicacion(country=request.json["country"], 
                                        city=request.json["city"], 
                                        description=request.json["description"], 
                                        empresaId=empresaId)
            db.session.add(nueva_ubicacion)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return ubicacion_schema.dump(nueva_ubicacion), 201


    
    def get(self, empresaId):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404
            
        try:
                return[ubicacion_schema.dump(t) for t in Ubicacion.query.filter(
                (Ubicacion.empresaId == empresaId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        
# Ubicacion
# Vista PATCH - GET - DELETE
class VistaUbicacion(Resource):

    def patch(self, empresaId, id):
        
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            ubicacion = Ubicacion.query.get(id)
            if ubicacion is None:
                return 'No existe la Ubicacion del empresa solicitada', 404


            if "country" in request.json:
                if request.json["country"] == "":
                    return 'El campo country es requerido', 400
                ubicacion.country = request.json["country"]

            if "city" in request.json:
                if request.json["city"] == "":
                    return 'El campo city es requerido', 400
                ubicacion.city = request.json["city"]

            if "description" in request.json:
                if request.json["description"] == "":
                    return 'El campo description es requerido', 400
                ubicacion.description = request.json["description"]

            try:
                db.session.commit()
                return ubicacion_schema.dump(ubicacion), 200
            except:
                db.session.rollback()
                return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, empresaId, id):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            ubicacion = Ubicacion.query.get(id)
            if ubicacion is None:
                return 'No existe la Ubicacion del empresa solicitada', 404
        return ubicacion_schema.dump(ubicacion), 200

    def delete(self, empresaId, id):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            ubicacion = Ubicacion.query.get(id)
            if ubicacion is None:
                return 'No existe la Ubicacion del empresa solicitada', 404
        try:
            db.session.delete(ubicacion)
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412



# Proyecto
# Vista POST - GET

class VistaProyectos(Resource):
    def post(self, empresaId):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404
        if not "proyecto" in request.json or not "description" in request.json:
            return 'Los campos proyecto, description son requeridos', 400
        if request.json["proyecto"] == "" or request.json["description"] == "": 
            return 'Los campos proyecto, description son requeridos', 400


        try:
            nueva_proyecto = Proyecto(proyecto=request.json["proyecto"], 
                                        description=request.json["description"], empresaId=empresaId)
            db.session.add(nueva_proyecto)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        
        return proyecto_schema.dump(nueva_proyecto), 201


    
    def get(self, empresaId):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404
            
        try:
                return[proyecto_schema.dump(t) for t in Proyecto.query.filter(
                (Proyecto.empresaId == empresaId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        
# Proyecto
# Vista PATCH - GET - DELETE
class VistaProyecto(Resource):

    def patch(self, empresaId, id):
        
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            proyecto = Proyecto.query.get(id)
            if proyecto is None:
                return 'No existe la Proyecto del empresa solicitada', 404


            if "proyecto" in request.json:
                if request.json["proyecto"] == "":
                    return 'El campo proyecto es requerido', 400
                proyecto.proyecto = request.json["proyecto"]

            if "description" in request.json:
                if request.json["description"] == "":
                    return 'El campo description es requerido', 400
                proyecto.description = request.json["description"]

            try:
                db.session.commit()
                return proyecto_schema.dump(proyecto), 200
            except:
                db.session.rollback()
                return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, empresaId, id):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            proyecto = Proyecto.query.get(id)
            if proyecto is None:
                return 'No existe la Proyecto del empresa solicitada', 404
        return proyecto_schema.dump(proyecto), 200

    def delete(self, empresaId, id):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            proyecto = Proyecto.query.get(id)
            if proyecto is None:
                return 'No existe la Proyecto del empresa solicitada', 404
        try:
            db.session.delete(proyecto)
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412



# Entrevistas
# Vista POST - GET
class VistaEntrevistas(Resource):
    
    def get(self, empresaId):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404
            
        try:
                return[entrevista_schema.dump(t) for t in Entrevista.query.filter(
                (Entrevista.empresaId == empresaId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412


# Entrevistas
# Vista POST - GET
class VistaAplicaciones(Resource):
    
    def get(self, empresaId):
        if empresaId.isnumeric() == False:
            return 'El empresaId no es un número.', 400
        else:
            empresa = Empresa.query.get(empresaId)
            if empresa is None:
                return 'No existe la cuenta del empresa solicitada', 404
            
        try:
                return[aplicacion_schema.dump(t) for t in Aplicacion.query.filter(
                (Aplicacion.empresaId == empresaId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
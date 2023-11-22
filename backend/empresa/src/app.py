from flask_restful import Api
from .modelos import db
from .vistas import VistaPing,VistaRegistro,VistaEmpresa,VistaVerticales, VistaVertical,VistaUbicacion,VistaUbicaciones, VistaProyecto, VistaProyectos, VistaEntrevistas, VistaAplicaciones
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask import Flask
from os import environ
import os

def create_app(config_name):
    app = Flask(__name__)  
    
    if 'SQLALCHEMY_DATABASE_URI' in environ:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI') if environ.get('SQLALCHEMY_DATABASE_URI') != 'default' else 'sqlite://'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS']=True
    return app

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaRegistro, '/empresa')
api.add_resource(VistaEmpresa, '/empresa/<string:id>')
api.add_resource(VistaVerticales, '/empresa/<string:empresaId>/vertical')
api.add_resource(VistaEntrevistas, '/empresa/<string:empresaId>/entrevista')
api.add_resource(VistaAplicaciones, '/empresa/<string:empresaId>/aplicacion')
api.add_resource(VistaVertical, '/empresa/<string:empresaId>/vertical/<string:id>')
api.add_resource(VistaUbicaciones, '/empresa/<string:empresaId>/ubicacion')
api.add_resource(VistaUbicacion, '/empresa/<string:empresaId>/ubicacion/<string:id>')
api.add_resource(VistaProyectos, '/empresa/<string:empresaId>/proyecto')
api.add_resource(VistaProyecto, '/empresa/<string:empresaId>/proyecto/<string:id>')
api.add_resource(VistaPing, '/empresa/ping')


from flask_restful import Api
from .modelos import db
from .vistas import VistaPing, VistaPerfil, VistaHabilidad, VistaPerfiles, VistaConocimientos, VistaConocimiento, VistaHabilidades, VistaIdiomas, VistaIdioma
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
api.add_resource(VistaPerfiles, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil')
api.add_resource(VistaPerfil, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:id>')
api.add_resource(VistaHabilidades, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/habilidad')
api.add_resource(VistaHabilidad, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/habilidad/<string:id>')
api.add_resource(VistaConocimientos, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/conocimiento')
api.add_resource(VistaConocimiento, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/conocimiento/<string:id>')
api.add_resource(VistaIdiomas, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/idioma')
api.add_resource(VistaIdioma, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/idioma/<string:id>')
api.add_resource(VistaPing, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/ping')


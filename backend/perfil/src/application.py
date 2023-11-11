from flask_restful import Api
from pathlib import Path
from modelos import db
from vistas import VistaPing, VistaPerfil, VistaHabilidad, VistaPerfiles, VistaConocimientos, VistaConocimiento, VistaHabilidades, VistaIdiomas, VistaIdioma
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask import Flask
from os import environ
import os

def create_app(config_name):
    application = Flask(__name__)
            
    parent_dir = Path(__file__).parent.parent.parent
    db_path = parent_dir / 'persistencia' / 'abc.db'  
    
    if 'SQLALCHEMY_DATABASE_URI' in environ:
        application.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI') if environ.get('SQLALCHEMY_DATABASE_URI') != 'default' else 'sqlite://'
    else:
        application.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    application.config['PROPAGATE_EXCEPTIONS']=True
    return application

application = create_app('default')
application_context = application.app_context()
application_context.push()

db.init_app(application)
db.create_all()

cors = CORS(application)

api = Api(application)
api.add_resource(VistaPerfiles, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil')
api.add_resource(VistaPerfil, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:id>')
api.add_resource(VistaHabilidades, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/habilidad')
api.add_resource(VistaHabilidad, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/habilidad/<string:id>')
api.add_resource(VistaConocimientos, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/conocimiento')
api.add_resource(VistaConocimiento, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/conocimiento/<string:id>')
api.add_resource(VistaIdiomas, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/idioma')
api.add_resource(VistaIdioma, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/idioma/<string:id>')
api.add_resource(VistaPing, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/ping')

if __name__ == '__main__':
    application.run(port=5003, debug=True)

from flask_restful import Api
from pathlib import Path
from modelos import db
from vistas import VistaPing,VistaRegistro,VistaEmpresa,VistaVerticales, VistaVertical,VistaUbicacion,VistaUbicaciones, VistaProyecto, VistaProyectos
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
api.add_resource(VistaRegistro, '/empresa')
api.add_resource(VistaEmpresa, '/empresa/<string:id>')
api.add_resource(VistaVerticales, '/empresa/<string:empresaId>/vertical')
api.add_resource(VistaVertical, '/empresa/<string:empresaId>/vertical/<string:id>')
api.add_resource(VistaUbicaciones, '/empresa/<string:empresaId>/ubicacion')
api.add_resource(VistaUbicacion, '/empresa/<string:empresaId>/ubicacion/<string:id>')
api.add_resource(VistaProyectos, '/empresa/<string:empresaId>/proyecto')
api.add_resource(VistaProyecto, '/empresa/<string:empresaId>/proyecto/<string:id>')
api.add_resource(VistaPing, '/empresa/ping')

if __name__ == '__main__':
    application.run(port=5002, debug=True)

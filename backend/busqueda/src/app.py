from flask_restful import Api
from .modelos import db
from .vistas import VistaPing, VistaBusqueda, VistaBusquedaes, VistaResultado, VistaResultados,VistaEjecuta
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
api.add_resource(VistaBusquedaes, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/busqueda')
api.add_resource(VistaEjecuta, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/busqueda/<string:id>/run', resource_class_kwargs={ 'app': app, 'db': db })
api.add_resource(VistaBusqueda, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/busqueda/<string:id>')
api.add_resource(VistaResultados, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/busqueda/<string:busquedaId>/resultado')
api.add_resource(VistaResultado, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/busqueda/<string:busquedaId>/resultado/<string:id>')
api.add_resource(VistaPing, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/ping')


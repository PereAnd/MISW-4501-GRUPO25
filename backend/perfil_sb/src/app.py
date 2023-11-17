from flask_restful import Api
from .vistas import  VistaPing, VistaConocimiento, VistaConocimientos, VistaHabilidades, VistaHabilidad, VistaIdioma, VistaIdiomas, VistaPerfil, VistaPerfiles
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask import Flask
from datetime import datetime, timedelta
from os import environ
from .breaker import CircuitBreaker
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
cors = CORS(app)

api = Api(app)


breaker = CircuitBreaker(exceptions=(Exception,), threshold=5, delay=10)

api.add_resource(VistaPerfiles, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaPerfil, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaHabilidades, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/habilidad', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaHabilidad, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/habilidad/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaConocimientos, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/conocimiento', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaConocimiento, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/conocimiento/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaIdiomas, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/idioma', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaIdioma, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/idioma/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaPing, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/ping', resource_class_kwargs={ 'breaker': breaker })


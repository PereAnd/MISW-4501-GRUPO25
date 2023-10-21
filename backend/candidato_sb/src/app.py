from flask_restful import Api
from .vistas import  VistaPing, VistaInformacionesTecnicas, VistaCandidato, VistaInformacionAcademica, VistaInformacionesAcademicas, VistaInformacionTecnica, VistaRegistro
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

api.add_resource(VistaRegistro, '/candidato', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaCandidato, '/candidato/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaInformacionesAcademicas, '/candidato/<string:candidatoId>/informacionAcademica', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaInformacionAcademica, '/candidato/<string:candidatoId>/informacionAcademica/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaInformacionesTecnicas, '/candidato/<string:candidatoId>/informacionTecnica', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaInformacionTecnica, '/candidato/<string:candidatoId>/informacionTecnica/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaPing, '/candidato/ping')

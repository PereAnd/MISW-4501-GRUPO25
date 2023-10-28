from flask_restful import Api
from .vistas import  VistaPing, VistaRegistro, VistaEmpresa, VistaVertical, VistaVerticales, VistaUbicaciones, VistaUbicacion #, VistaInformacionesTecnicas, VistaCandidato, VistaInformacionAcademica, VistaInformacionesAcademicas, VistaInformacionTecnica, VistaRegistro, VistaInformacionesLaborales, VistaInformacionLaboral
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

api.add_resource(VistaRegistro, '/empresa', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaEmpresa, '/empresa/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaVerticales, '/empresa/<string:empresaId>/vertical', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaVertical, '/empresa/<string:empresaId>/vertical/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaUbicaciones, '/empresa/<string:empresaId>/ubicacion', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaUbicacion, '/empresa/<string:empresaId>/ubicacion/<string:id>', resource_class_kwargs={ 'breaker': breaker })
# api.add_resource(VistaInformacionesTecnicas, '/candidato/<string:candidatoId>/informacionTecnica', resource_class_kwargs={ 'breaker': breaker })
# api.add_resource(VistaInformacionTecnica, '/candidato/<string:candidatoId>/informacionTecnica/<string:id>', resource_class_kwargs={ 'breaker': breaker })
# api.add_resource(VistaInformacionesLaborales, '/candidato/<string:candidatoId>/informacionLaboral', resource_class_kwargs={ 'breaker': breaker })
# api.add_resource(VistaInformacionLaboral, '/candidato/<string:candidatoId>/informacionLaboral/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaPing, '/empresa/ping')

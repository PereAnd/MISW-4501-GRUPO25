from flask_restful import Api
from .vistas import  VistaPing, VistaBusqueda, VistaBusquedaes, VistaResultado, VistaResultados, VistaEjecuta
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

api.add_resource(VistaBusquedaes, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/busqueda', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaBusqueda, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/busqueda/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaResultados, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/busqueda/<string:busquedaId>/resultado', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaResultado, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/busqueda/<string:busquedaId>/resultado/<string:id>', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaPing, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/ping', resource_class_kwargs={ 'breaker': breaker })
api.add_resource(VistaEjecuta, '/empresa/<string:empresaId>/proyecto/<string:proyectoId>/perfil/<string:perfilId>/busqueda/<string:id>/run', resource_class_kwargs={ 'breaker': breaker })



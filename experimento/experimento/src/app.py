from flask_restful import Api
from .modelos import db
from .vistas import VistaExperimento, VistaPing, VistaExperimentos
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask import Flask
from datetime import datetime, timedelta
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
api.add_resource(VistaExperimentos, '/experimento/')
api.add_resource(VistaExperimento, '/experimento/<string:id>')
api.add_resource(VistaPing, '/experimento/ping/')


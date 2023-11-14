from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, auto_field, fields

db = SQLAlchemy()

class Aplicacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicationDate = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    proyectoId = db.Column(db.Integer, nullable=False)
    empresaId = db.Column(db.Integer, nullable=False)
    perfilId = db.Column(db.Integer, nullable=False)
    candidatoId = db.Column(db.Integer, nullable=False)
    entrevistas = db.relationship('Entrevista', backref='aplicacion')

class Entrevista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enterviewDate = db.Column(db.DateTime, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    feedback = db.Column(db.Text, nullable=True)
    aplicacionId = db.Column(db.Integer, db.ForeignKey('aplicacion.id'))

class EntrevistaEschema(SQLAlchemySchema):
    class Meta:
         model = Entrevista
         include_relationships = False
         load_instance = True         
    id = auto_field()
    enterviewDate = auto_field()
    done = auto_field()
    feedback = auto_field()
    aplicacionId = auto_field()

class AplicacionEschema(SQLAlchemySchema):
    class Meta:
         model = Aplicacion
         include_relationships = True
         load_instance = True         
    id = auto_field()
    applicationDate = auto_field()
    status = auto_field()
    perfilId = auto_field()
    candidatoId = auto_field()
    entrevistas = fields.Nested(EntrevistaEschema(many=True), many=True)

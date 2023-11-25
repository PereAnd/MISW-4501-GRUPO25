from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, auto_field, fields

db = SQLAlchemy()

class Busqueda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    searchDate = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    proyectoId = db.Column(db.Integer, nullable=False)
    empresaId = db.Column(db.Integer, nullable=False)
    perfilId = db.Column(db.Integer, nullable=False)
    resultados = db.relationship('Resultado', backref='busqueda')

class Resultado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proyectoId = db.Column(db.Integer, nullable=False)
    empresaId = db.Column(db.Integer, nullable=False)
    perfilId = db.Column(db.Integer, nullable=False)
    busquedaId = db.Column(db.Integer, db.ForeignKey('busqueda.id'))
    candidatoId = db.Column(db.Integer, nullable=False)

class ResultadoEschema(SQLAlchemySchema):
    class Meta:
         model = Resultado
         include_relationships = False
         load_instance = True         
    id = auto_field()
    busquedaId = auto_field()
    candidatoId = auto_field()

class BusquedaEschema(SQLAlchemySchema):
    class Meta:
         model = Busqueda
         include_relationships = True
         load_instance = True         
    id = auto_field()
    searchDate = auto_field()
    status = auto_field()
    perfilId = auto_field()
    resultados = fields.Nested(ResultadoEschema(many=True), many=True)

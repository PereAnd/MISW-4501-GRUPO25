from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, auto_field, fields

db = SQLAlchemy()

class Perfil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(120),unique=True, nullable=False)
    years = db.Column(db.Integer, nullable=True)
    proyectoId = db.Column(db.Integer, db.ForeignKey('perfil.id'))
    habilidades = db.relationship('Habilidad', backref='perfil')
    conocimientos = db.relationship('Conocimiento', backref='perfil')
    idiomas = db.relationship('Idioma', backref='perfil')

class Habilidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    perfilId = db.Column(db.Integer, db.ForeignKey('perfil.id'))

class Conocimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    perfilId = db.Column(db.Integer, db.ForeignKey('perfil.id'))

class Idioma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    perfilId = db.Column(db.Integer, db.ForeignKey('perfil.id'))


class IdiomaEschema(SQLAlchemySchema):
    class Meta:
         model = Idioma
         include_relationships = False
         load_instance = True         
    id = auto_field()
    name = auto_field()
    description = auto_field()
    perfilId = auto_field()


class HabilidadEschema(SQLAlchemySchema):
    class Meta:
         model = Habilidad
         include_relationships = False
         load_instance = True         
    id = auto_field()
    name = auto_field()
    description = auto_field()
    perfilId = auto_field()

class ConocimientoEschema(SQLAlchemySchema):
    class Meta:
         model = Conocimiento
         include_relationships = False
         load_instance = True         
    id = auto_field()
    name = auto_field()
    description = auto_field()
    perfilId = auto_field()

class PerfilEschema(SQLAlchemySchema):
    class Meta:
         model = Perfil
         include_relationships = True
         load_instance = True         
    id = auto_field()
    name = auto_field()
    role = auto_field()
    location = auto_field()
    years = auto_field()
    habilidades = fields.Nested(HabilidadEschema(many=True), many=True)
    conocimientos = fields.Nested(ConocimientoEschema, many=True)
    idiomas = fields.Nested(IdiomaEschema, many=True)

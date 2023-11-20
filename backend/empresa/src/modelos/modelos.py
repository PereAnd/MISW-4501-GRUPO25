from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, auto_field, fields

db = SQLAlchemy()


class Entrevista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enterviewDate = db.Column(db.DateTime, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    feedback = db.Column(db.Text, nullable=True)
    proyectoId = db.Column(db.Integer, nullable=False)
    empresaId = db.Column(db.Integer, nullable=False)
    perfilId = db.Column(db.Integer, nullable=False)
    aplicacionId = db.Column(db.Integer, nullable=False)




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
    proyectoId = auto_field()
    empresaId = auto_field()
    perfilId = auto_field()


class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proyecto = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    empresaId = db.Column(db.Integer, db.ForeignKey('empresa.id'))

class ProyectoEschema(SQLAlchemySchema):
    class Meta:
         model = Proyecto
         include_relationships = False
         load_instance = True         
    id = auto_field()
    proyecto = auto_field()
    description = auto_field()


class Vertical(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vertical = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    empresaId = db.Column(db.Integer, db.ForeignKey('empresa.id'))

class VerticalEschema(SQLAlchemySchema):
    class Meta:
         model = Vertical
         include_relationships = False
         load_instance = True         
    id = auto_field()
    vertical = auto_field()
    description = auto_field()

class Ubicacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    empresaId = db.Column(db.Integer, db.ForeignKey('empresa.id'))

class UbicacionEschema(SQLAlchemySchema):
    class Meta:
         model = Ubicacion
         include_relationships = False
         load_instance = True         
    id = auto_field()
    country = auto_field()
    city = auto_field()
    description = auto_field()


class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    mail = db.Column(db.String(150), nullable=False)
    docType = db.Column(db.String(10), nullable=True)
    docNumber = db.Column(db.String(30), nullable=True)
    organizationType = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    vertical = db.relationship('Vertical', backref='verticalRel')
    ubicacion = db.relationship('Ubicacion', backref='ubicacion')
    proyecto = db.relationship('Proyecto', backref='proyectoRel')




class EmpresaEschema(SQLAlchemySchema):
    class Meta:
         model = Empresa
         include_relationships = True
         load_instance = True         
    id = auto_field()
    name = auto_field()
#     lastNames = auto_field()
    mail = auto_field()
    docType = auto_field()
    docNumber = auto_field()
    organizationType = auto_field()
    description = auto_field()
    vertical = fields.Nested(VerticalEschema, many=True)
    ubicacion = fields.Nested(UbicacionEschema, many=True)
#     docType = auto_field()
#     docNumber = auto_field()
#     phone = auto_field()
#     address = auto_field()
#     birthDate = auto_field()
#     country = auto_field()
#     city = auto_field()
#     language = auto_field()
#     informacionAcademica = fields.Nested(InformacionAcademicaEschema(many=True), many=True)
#     informacionTecnica = fields.Nested(InformacionTecnicaEschema, many=True)
#     informacionLaboral = fields.Nested(InformacionLaboralEschema, many=True)

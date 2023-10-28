from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, auto_field, fields

db = SQLAlchemy()


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


# class InformacionAcademica(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), nullable=False)
#     institution = db.Column(db.String(50), nullable=False)
#     beginDate = db.Column(db.DateTime, nullable=False)
#     endDate = db.Column(db.DateTime, nullable=True)
#     studyType = db.Column(db.String(50), nullable=True)
#     candidatoId = db.Column(db.Integer, db.ForeignKey('candidato.id'))

# class InformacionTecnica(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(20), nullable=False)
#     description = db.Column(db.String(150), nullable=False)
#     candidatoId = db.Column(db.Integer, db.ForeignKey('candidato.id'))

# class InformacionLaboral(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     position = db.Column(db.String(150), nullable=False)
#     organization = db.Column(db.String(150), nullable=False)
#     activities = db.Column(db.Text, nullable=False)
#     dateFrom = db.Column(db.DateTime, nullable=False)
#     dateTo = db.Column(db.DateTime, nullable=True)
#     candidatoId = db.Column(db.Integer, db.ForeignKey('candidato.id'))


# class InformacionLaboralEschema(SQLAlchemySchema):
#     class Meta:
#          model = InformacionLaboral
#          include_relationships = False
#          load_instance = True         
#     id = auto_field()
#     position = auto_field()
#     organization = auto_field()
#     activities = auto_field()
#     dateFrom = auto_field()
#     dateTo = auto_field()
#     candidatoId = auto_field()


# class InformacionAcademicaEschema(SQLAlchemySchema):
#     class Meta:
#          model = InformacionAcademica
#          include_relationships = False
#          load_instance = True         
#     id = auto_field()
#     title = auto_field()
#     institution = auto_field()
#     beginDate = auto_field()
#     endDate = auto_field()
#     studyType = auto_field()
#     candidatoId = auto_field()

# class InformacionTecnicaEschema(SQLAlchemySchema):
#     class Meta:
#          model = InformacionTecnica
#          include_relationships = False
#          load_instance = True         
#     id = auto_field()
#     type = auto_field()
#     description = auto_field()
#     candidatoId = auto_field()

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

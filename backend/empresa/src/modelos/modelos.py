from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, auto_field, fields

db = SQLAlchemy()


class Aplicacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicationDate = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    result =  db.Column(db.Text, nullable=False)
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
    proyectoId = db.Column(db.Integer, nullable=False)
    empresaId = db.Column(db.Integer, nullable=False)
    perfilId = db.Column(db.Integer, nullable=False)
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
    proyectoId = auto_field()
    empresaId = auto_field()
    perfilId = auto_field()


class AplicacionEschema(SQLAlchemySchema):
    class Meta:
         model = Aplicacion
         include_relationships = True
         load_instance = True         
    id = auto_field()
    applicationDate = auto_field()
    status = auto_field()
    result = auto_field()
    perfilId = auto_field()
    proyectoId = auto_field()
    candidatoId = auto_field()
    entrevistas = fields.Nested(EntrevistaEschema(many=True), many=True)

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
    mail = auto_field()
    docType = auto_field()
    docNumber = auto_field()
    organizationType = auto_field()
    description = auto_field()
    vertical = fields.Nested(VerticalEschema, many=True)
    ubicacion = fields.Nested(UbicacionEschema, many=True)


class DatosCombinados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empresaId = db.Column(db.Integer, nullable=False)
    proyectoId = db.Column(db.Integer, nullable=False)
    perfilId = db.Column(db.Integer, nullable=False)
    candidatoId = db.Column(db.Integer, nullable=False)
    fullName=db.Column(db.String(50), nullable=False)
    applicationDate = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    enterviewDate = db.Column(db.DateTime, nullable=False)
    result = db.Column(db.Text, nullable=False)
    feedback = db.Column(db.Text, nullable=True)
    
class DatosCombinadosEsquema(SQLAlchemySchema):
    class Meta:
        model = DatosCombinados
        include_relationships = False
        load_instance = True

    id = auto_field()
    fullName = auto_field()
    applicationDate = auto_field()
    enterviewDate = auto_field()
    status = auto_field()
    enterviewDate = auto_field()
    result = auto_field()
    feedback = auto_field()
    

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(50), nullable=False)
    lastNames = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    docType = db.Column(db.String(10), nullable=True)
    docNumber = db.Column(db.String(30), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    birthDate = db.Column(db.DateTime, nullable=True)
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    language = db.Column(db.String(50))

class CandidatoEschema(SQLAlchemySchema):
    class Meta:
         model = Candidato
         include_relationships = True
         load_instance = True         
    id = auto_field()
    names = auto_field()
    lastNames = auto_field()
    mail = auto_field()
    docType = auto_field()
    docNumber = auto_field()
    phone = auto_field()
    address = auto_field()
    birthDate = auto_field()
    country = auto_field()
    city = auto_field()
    language = auto_field()
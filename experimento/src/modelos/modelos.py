from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Experimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor1 = db.Column(db.Integer)
    valor2 = db.Column(db.String(140))
    valor3 = db.Column(db.DateTime)


class ExperimentoSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Experimento
         include_relationships = True
         load_instance = True         

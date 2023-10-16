from flask_restful import Resource
from flask import request
from ..modelos import db, Experimento, ExperimentoSchema
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import requests, sys

experimento_schema = ExperimentoSchema()

class VistaExperimentos(Resource):

    def post(self):
        if not "valor1" in request.json or not "valor2" in request.json or not "valor3" in request.json:
            return 'los campos valor1, valor2 y valor3 son requeridos.', 400

        if request.json["valor2"] == "" or request.json["valor3"] == "":
            return 'los campos valor1, valor2 y valor3 son requeridos.', 400

#        try:

        valor3 = datetime.strptime(request.json["valor3"], '%d/%m/%Y %H:%M:%S')

        nuevo_experimento = Experimento(valor1=request.json["valor1"], 
                                    valor2=request.json["valor2"],
                                    valor3=valor3)

        db.session.add(nuevo_experimento)
        db.session.commit()
#        except:
#            db.session.rollback()
#            return {'Error': str(sys.exc_info()[0])}, 412
        return {'id':nuevo_experimento.id, 'valor1': nuevo_experimento.valor1, 'valor2': nuevo_experimento.valor2, 'valor3':nuevo_experimento.valor3.isoformat()}, 201

    def get(self):


        valor1 = request.args.get('valor1', default = -1, type=int)
        valor2 = request.args.get('valor2', default = "none", type = str)
        valor3 = request.args.get('valor3', default = "none", type = str)

        try:
            if valor3 != "none":
                try:
                    valor3date = datetime.strptime(valor3, '%d/%m/%Y %H:%M:%S')
                except:
                    return {'Error': 'La fecha tiene un formato incorrecto'}, 412

                return[experimento_schema.dump(t) for t in Experimento.query.filter(
                (Experimento.valor1 == valor1) | (valor1== -1)).filter((Experimento.valor2 == valor2) | (valor2== "none")).filter(
                (Experimento.valor3 == datetime.strptime(valor3, '%d/%m/%Y %H:%M:%S')) | (valor3== "none")).all()], 200 
            else:
                return[experimento_schema.dump(t) for t in Experimento.query.filter(
                (Experimento.valor1 == valor1) | (valor1== -1)).filter((Experimento.valor2 == valor2) | (valor2== "none"))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412




class VistaExperimento(Resource):

    def get(self, id):
        
        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            experimento = Experimento.query.get(id)
            if experimento is None:
                return 'No existe la publicación con ese identificador.', 404
            
            return experimento_schema.dump(experimento), 200

    def patch(self, id):
        
        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            experimento = Experimento.query.get(id)
            if experimento is None:
                return 'No existe la publicación con ese identificador.', 404
            else:
                if "valor1" in request.json:
                    experimento.valor1 = request.json["valor1"]

                if "valor2" in request.json:
                    experimento.valor2 = request.json["valor2"]

                try:

                    if "valor3" in request.json:
                        valor3 = datetime.strptime(request.json["valor3"], '%d/%m/%Y %H:%M:%S')
                        experimento.valor3 = valor3
                    db.session.commit()
                    return experimento_schema.dump(experimento), 200
                except:
                    db.session.rollback()
                    return {'Error': str(sys.exc_info()[0])}, 412

    def delete(self, id):
        
        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            experimento = Experimento.query.get(id)
            if experimento is None:
                return 'No existe la publicación con ese identificador.', 404
            else:
                db.session.delete(experimento)
                db.session.commit()
                return 'Se eliminó el registro', 200
 

class VistaPing(Resource):
    def get(self):
        return "pong"            

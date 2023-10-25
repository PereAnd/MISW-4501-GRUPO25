# Informacion Laboral
# Vista POST - GET
class VistaInformacionesLaborales(Resource):
    def post(self, candidatoId):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404
            
        if not "position" in request.json or not "organization" in request.json or not "activities" in request.json  or not "dateFrom" in request.json:
            return 'Los campos position, organization, activities y dateFrom son requeridos', 400
        if request.json["position"] == "" or request.json["organization"] == "" or request.json["activities"] == "": 
            return 'Los campos position, organization, activities y dateFrom son requeridos', 400

        try:
            dateFrom = datetime.strptime(request.json["dateFrom"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            return "El campo dateFrom no tiene formato de fecha correcto", 400

        dateTo = None
        if "dateTo" in request.json:
            if request.json["description"] != None:
                try:
                    dateTo = datetime.strptime(request.json["dateTo"], "%Y-%m-%dT%H:%M:%S.%fZ")
                except:
                    return "El campo dateTo no tiene formato de fecha correcto", 400
                
        
                





        try:
            nueva_informacion = InformacionLaboral(position=request.json["position"], 
                                        organization=request.json["organization"],
                                        activities=request.json["activities"],
                                        dateFrom=dateTo,
                                        dateTo=dateTo,
                                        candidatoId=candidatoId)
            db.session.add(nueva_informacion)
            db.session.commit()
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412
        return informacionLaboral_schema.dump(nueva_informacion), 201
    
    def get(self, candidatoId):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404
            
        try:
                return[informacionLaboral_schema.dump(t) for t in InformacionLaboral.query.filter(
                (InformacionLaboral.candidatoId == candidatoId))], 200
        except:
            return {'Error': str(sys.exc_info()[0])}, 412
        
# Informacion Laboral
# Vista PATCH - GET - DELETE
class VistaInformacionLaboral(Resource):

    def patch(self, candidatoId, id):
        
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            informacionLaboral = InformacionLaboral.query.get(id)
            if informacionLaboral is None:
                return 'No existe la Información Laboral del candidato solicitada', 404


            if "position" in request.json:
                if request.json["position"] == "":
                    return 'El campo position es requerido', 400
                informacionLaboral.position = request.json["position"]

            if "organization" in request.json:
                if request.json["organization"] == "":
                    return 'El campo organization es requerido', 400
                informacionLaboral.organization = request.json["organization"]

            if "activities" in request.json:
                if request.json["activities"] == "":
                    return 'El campo activities es requerido', 400
                informacionLaboral.activities = request.json["activities"]


            if "dateFrom" in request.json:
                if request.json["dateFrom"] == "":
                    return 'El campo dateFrom es requerido', 400
                try:
                    dateFrom = datetime.strptime(request.json["dateFrom"], "%Y-%m-%dT%H:%M:%S.%fZ")
                except:
                    return "El campo dateFrom no tiene formato de fecha correcto", 400

                informacionLaboral.dateFrom = dateFrom

            dateTo = None
            if "dateTo" in request.json:
                if request.json["dateTo"] != "" and request.json["dateTo"] != None :
                    try:
                        dateFrom = datetime.strptime(request.json["dateTo"], "%Y-%m-%dT%H:%M:%S.%fZ")
                    except:
                        return "El campo dateTo no tiene formato de fecha correcto", 400
                informacionLaboral.dateTo = dateTo

            try:
                db.session.commit()
                return informacionLaboral_schema.dump(informacionLaboral), 200
            except:
                db.session.rollback()
                return {'Error': str(sys.exc_info()[0])}, 412
                
    def get(self, candidatoId, id):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            informacionLaboral = InformacionLaboral.query.get(id)
            if informacionLaboral is None:
                return 'No existe la Información Laboral del candidato solicitada', 404
        return informacionLaboral_schema.dump(informacionLaboral), 200


    def delete(self, candidatoId, id):
        if candidatoId.isnumeric() == False:
            return 'El candidatoId no es un número.', 400
        else:
            candidato = Candidato.query.get(candidatoId)
            if candidato is None:
                return 'No existe la cuenta del candidato solicitada', 404

        if id.isnumeric() == False:
            return 'El id no es un número.', 400
        else:
            informacionLaboral = InformacionLaboral.query.get(id)
            if informacionLaboral is None:
                return 'No existe la Información Laboral del candidato solicitada', 404
        try:
            db.session.delete(informacionLaboral)
            db.session.commit()
            return 'Registro Eliminado Correctamente', 204
        except:
            db.session.rollback()
            return {'Error': str(sys.exc_info()[0])}, 412



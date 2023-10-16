export class InfoAcademica {
  constructor(
    public tittle: string,
    public institution: string,
    public beginDate: string,
    public endDate: string,
    public studyType: string,
    public candidatoId: number
  ) { }
}
/*

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(50), nullable=False)
    lastNames = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    docType = db.Column(db.String(10), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    birthDate = db.Column(db.DateTime, nullable=True)
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    language = db.Column(db.String(50))
    informacionAcademica = db.relationship('InformacionAcademica', backref='candidato')
    informacionTecnica = db.relationship('InformacionTecnica', backref='candidato')

class InformacionAcademica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(50), nullable=False)
    institution = db.Column(db.String(50), nullable=False)
    beginDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=True)
    studyType = db.Column(db.String(50), nullable=True)
    candidatoId = db.Column(db.Integer, db.ForeignKey('candidato.id'))

class InformacionTecnica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    candidatoId = db.Column(db.Integer, db.ForeignKey('candidato.id'))

*/

import { InfoAcademica } from "./info-academica";
import { InfoTecnica } from "./info-tecnica";

export class Candidato {
  constructor(
    public names: string,
    public lastNames: string,
    public mail: string,
    public password?: string,
    public confirmPassword?: string,
    public docType?: string,
    public docNumber?: string,
    public phone?: string,
    public address?: string,
    public birthDate?: Date,
    public country?: string,
    public city?: string,
    public language?: string,
    public id?: number,
    public informacionAcademica?: InfoAcademica[],
    public informacionTecnica?: InfoTecnica[]
  ) { }
}

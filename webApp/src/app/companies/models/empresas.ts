export class Empresa {
  constructor(
    public name: string,
    public mail: string,
    public password?: string,
    public confirmPassword?: string,
    public organizationType?: string,
    public docType?: string,
    public docNumber?: string,
    public description?: string,
    public id?: number
  ) { }
}

export class Ubicacion {
  constructor(
    public country: string,
    public city: string,
    public description: string,
    public id?: number
  ){}
}

export class Vertical {
  constructor (
    public vertical: string,
    public description: string,
    public id?: number
  ){ }
}

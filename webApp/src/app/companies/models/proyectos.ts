export class Proyecto {
  constructor(
    public proyecto: string,
    public description: string,
    public id?: number
  ){}
}

export class Perfil {
  constructor(
    public name: string,
    public role: string,
    public location: string,
    public years: number,
    public conocimientos?: Competencia[],
    public habilidades?: Competencia[],
    public idiomas?: Competencia[],
    public id?: number,
  ){}
}

export class Competencia {
  constructor(
    public name: string,
    public description: string,
    public id?: number
  ){}
}

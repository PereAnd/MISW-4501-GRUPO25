export class Perfil {
  constructor(
    public name: string,
    public role: string,
    public location: string,
    public years: number,
    public id?: number,
    public idiomas?: Competencia[],
    public conocimientos?: Competencia[],
    public habilidades?: Competencia[],
  ){}
}

export class Competencia {
  constructor(
    public name: string,
    public description: string,
    public id?: number
  ){}
}

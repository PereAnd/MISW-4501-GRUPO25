export class Empresa {
  constructor(
    public name: string,
    public mail: string,
    public password?: string,
    public confirmPassword?: string
  ) { }
}

import { Component } from '@angular/core';
import { RegCandidatoService } from '../../services/reg-candidato.service';
import { Candidato } from '../../models/candidato';

@Component({
  selector: 'app-reg-candidato',
  templateUrl: './reg-candidato.component.html',
  styleUrls: ['./reg-candidato.component.css']
})
export class RegCandidatoComponent {

  name: string = '';
  lastName: string = '';
  email: string = '';
  password: string = '';
  passwordConfirm: string = '';

  constructor(
    private regCandidatoService: RegCandidatoService
  ) {}

  registrarCandidato(){
    const newCandidato = new Candidato(this.name, this.lastName, this.email, this.password, this.passwordConfirm);
    console.log("Guardando nuevo candidato" + newCandidato);
    this.regCandidatoService.agregarCandidato(newCandidato);
  }
}

import { Component, OnInit } from '@angular/core';
import { RegCandidatoService } from '../../../services/reg-candidato.service';
import { Candidato } from '../../../models/candidato';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-reg-candidato',
  templateUrl: './reg-candidato.component.html',
  styleUrls: ['./reg-candidato.component.css']
})
export class RegCandidatoComponent implements OnInit{

  formCandidato: FormGroup;

  names: string = '';
  lastName: string = '';
  email: string = '';
  password: string = '';
  passwordConfirm: string = '';

  constructor(
    private regCandidatoService: RegCandidatoService,
    private formBuilder: FormBuilder,
  ) {}

  ngOnInit(): void {
    this.formCandidato = this.formBuilder.group({
      names: ['', Validators.required],
      lastName: ['', Validators.required],
      email: ['', Validators.required],
      password: ['', [Validators.required, Validators.minLength(5)]],
      passwordConfirm: ['', Validators.required]
    })
  }

  registrarCandidato(){
    const newCandidato = new Candidato(
      this.formCandidato.value.names,
      this.formCandidato.value.lastName,
      this.formCandidato.value.email,
      this.formCandidato.value.password,
      this.formCandidato.value.passwordConfirm
      );
    this.regCandidatoService.registrarCandidato(newCandidato)
      .subscribe({
        next: data => console.log("Candidato registrado", data),
        error: error => console.log("Error registrando el candidato", error)
      })
      this.formCandidato.reset();
  }
}

import { Component, OnInit } from '@angular/core';
import { RegCandidatoService } from '../../services/reg-candidato.service';
import { Candidato } from '../../models/candidato';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

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
    private router: Router
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
        next: data => {
          console.log("Candidato registrado")
          try {
              localStorage.setItem('candidatoId', (data as any).id)
              this.router.navigate(['/candidatos/dashboard/' + localStorage.getItem('candidatoId') + '/info-personal'])
            } catch (error) {
              alert('Error registrando el candidato')
              console.log("Error registrando el candidato", error)
            }
        },
        error: error => console.log("Error registrando el candidato", error),
      })
  }
}

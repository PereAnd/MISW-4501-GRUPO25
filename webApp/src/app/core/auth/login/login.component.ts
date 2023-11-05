import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginService } from '../services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  roles = ['Candidato', 'Empresa']

  constructor(
    private router: Router,
    private loginService: LoginService
  ){ }

  formLogin: FormGroup = new FormGroup({
    email: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required),
    role: new FormControl('', Validators.required)
  })

  get email() { return this.formLogin.get('email') }
  get password() { return this.formLogin.get('password') }
  get role() { return this.formLogin.get('role') }

  login(){
    if(this.formLogin.value.role == 'Candidato'){
      this.loginService.loginCandidatos(this.formLogin.value.email).subscribe({
        next: data => {
          try {
            localStorage.setItem('candidatoId', (data as any)[0].id)
            this.router.navigate(['/candidatos/dashboard/' + localStorage.getItem('candidatoId') + '/info-personal'])
          } catch (error) {
            alert('Usuario o contraseña no válidos')
          }
        }, error: e => {
          alert('Usuario o contraseña no válidos')
        }
      })
    } else if (this.formLogin.value.role == 'Empresa') {
      this.loginService.loginEmpresas(this.formLogin.value.email).subscribe({
        next: data => {
          try {
            localStorage.setItem('empresaId', (data as any)[0].id)
            this.router.navigate(['/empresas/dashboard/' + localStorage.getItem('empresaId') + '/info-general'])

          } catch (error) {
            alert('Usuario o contraseña no válidos')
          }
        }, error: e => {
          alert('Usuario o contraseña no válidos')
        }
      })
    }
  }
}

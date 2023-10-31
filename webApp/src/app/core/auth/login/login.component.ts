import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  roles = ['Candidato', 'Empresa']

  constructor(
    private router: Router
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
    console.log(this.formLogin.value)
    if(this.formLogin.value.role == 'Candidato'){
      this.router.navigate(['/candidatos/dashboard/1'])
    } else if (this.formLogin.value.role == 'Empresa') {
      this.router.navigate(['/empresas/dashboard'])
    }
  }
}

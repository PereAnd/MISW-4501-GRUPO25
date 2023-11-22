import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Empresa } from '../../models/empresas';
import { RegEmpresaService } from '../../services/reg-empresa.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-reg-empresa',
  templateUrl: './reg-empresa.component.html',
  styleUrls: ['./reg-empresa.component.css']
})
export class RegEmpresaComponent implements OnInit {
  formEmpresas: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private regEmpresaService: RegEmpresaService,
    private router: Router
  ){ }

  get name() { return this.formEmpresas.get('name') }
  get email() { return this.formEmpresas.get('email') }
  get password() { return this.formEmpresas.get('password') }
  get confirmPassword() { return this.formEmpresas.get('confirmPassword') }

  ngOnInit(): void {
    this.formEmpresas = this.formBuilder.group({
      name: ['', Validators.required],
      email: ['', Validators.required],
      password: ['', [Validators.required, Validators.minLength(5)]],
      confirmPassword: ['', Validators.required]
    })
  }

  registrarEmpresa(){
    const newEmpresa = new Empresa(
      this.formEmpresas.value.name,
      this.formEmpresas.value.email,
      this.formEmpresas.value.password,
      this.formEmpresas.value.confirmPassword
    );

    this.regEmpresaService.registrarEmpresa(newEmpresa).subscribe({
      next: data => {
        console.log("Empresa registrada correctamente");
        try {
          localStorage.setItem('empresaId', (data as any).id)
          this.router.navigate(['/empresas/dashboard/' + localStorage.getItem('empresaId') + '/info-general'])
        } catch (error) {
          alert('Error registrando la empresa')
          console.log("Error registrando la empresa", error)
        }
      },
      error: error => console.log("Error registrando la empresa", error),
    })
  }
}

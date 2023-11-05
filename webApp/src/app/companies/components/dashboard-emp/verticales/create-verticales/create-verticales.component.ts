import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { InfoTecnica } from 'src/app/candidates/models/info-tecnica';
import { InfTecnicaService } from 'src/app/candidates/services/inf-tecnica.service';
import { Vertical } from 'src/app/companies/models/vertical';
import { VerticalesService } from 'src/app/companies/services/verticales.service';

@Component({
  selector: 'app-create-verticales',
  templateUrl: './create-verticales.component.html',
  styleUrls: ['./create-verticales.component.css']
})
export class CreateVerticalesComponent {
  indexVertical: number;
  empresaId: number;
  formVerticales: FormGroup = new FormGroup({
  vertical: new FormControl('', Validators.required),
  description: new FormControl('', Validators.required)
  })

  listVerticales: string[] = ['Desarrollo de Software', 'Proveedor de hardware', 'Empresa de Ciberseguridad', 'Consultoría de TI', 'Telecomunicaciones', 'E-Commerce', 'Empresa de Big Data y Análisis de Datos', 'IA y Aprendizaje Automático', 'Infraestructura de Red'];

  get vertical() { return this.formVerticales.get('vertical') }
  get description() { return this.formVerticales.get('description') }

  constructor(
    private verticalesService: VerticalesService,
    private router: Router,
    private route: ActivatedRoute
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    this.indexVertical = this.route.snapshot.params['idv'];
    if(this.indexVertical){
      this.verticalesService.findVertical(this.empresaId, this.indexVertical)
      .subscribe({
        next: data => {
          this.formVerticales.setValue({
            vertical: data.vertical,
            description: data.description
          })
        },
        error: error => console.error('Error obteniendo la vertical seleccionada', error)
      })
    }
  }

  registrarVertical(){
    const newVertical = new Vertical(
    this.formVerticales.value.vertical,
    this.formVerticales.value.description
    )
    if(!this.indexVertical){
      this.verticalesService.addVertical(newVertical, this.empresaId).subscribe({
          next: data => {
            console.log("Vertical registrada")
            this.formVerticales.reset();
          },
          error: error => {
            console.log("Error registrando la Vertical", error)
            alert('Error registrando la Vertical')
          },
          complete: () => {
            this.router.navigate(['..'], {relativeTo: this.route})
          }
        })
    } else {
      this.verticalesService.editVertical(newVertical, this.indexVertical, this.empresaId).subscribe({
        next: data => {
          console.log('Vertical editada')
          this.formVerticales.reset()
        },
        error: error => {
          console.log('Error editando la Vertical', error)
          alert('Error editando la Vertical')
        },
        complete: () => {
          this.router.navigate(['..'], {relativeTo: this.route})
        }
      })
    }
  }

  cancelarCreacion(){
    this.formVerticales.reset()
  }
}

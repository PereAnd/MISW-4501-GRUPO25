import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { InfoTecnica } from 'src/app/candidates/models/info-tecnica';
import { InfTecnicaService } from 'src/app/candidates/services/inf-tecnica.service';

@Component({
  selector: 'app-create-info-tec',
  templateUrl: './create-info-tec.component.html',
  styleUrls: ['./create-info-tec.component.css']
})
export class CreateInfoTecComponent {
  indexInfoTec: number;

  formInfoTecnica: FormGroup = new FormGroup({
    type: new FormControl('', Validators.required),
    description: new FormControl('', Validators.required)
  })

  tiposInfoTecnica = ['Conocimiento', 'Habilidad']

  get type() { return this.formInfoTecnica.get('type') }
  get description() { return this.formInfoTecnica.get('description') }

  constructor(
    private infTecnicaService: InfTecnicaService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.indexInfoTec = this.route.snapshot.params['idit'];
    if(this.indexInfoTec){
      this.infTecnicaService.findInfoTecnica(1, this.indexInfoTec)
      .subscribe({
        next: data => {
          this.formInfoTecnica.setValue({
            type: data.type,
            description: data.description
          })
        },
        error: error => console.error('Error obteniendo la información técnica seleccionada', error)
      })
    }
  }

  registrarInfoTecnica(){
    const candidatoId: number = 1;
    const newInfoTecnica = new InfoTecnica(
      this.formInfoTecnica.value.type,
      this.formInfoTecnica.value.description,
      1 // OBTENER ID DEL CANDIDATO ACTUAL
    )
    if(!this.indexInfoTec){
      this.infTecnicaService.addInfoTecnica(newInfoTecnica, candidatoId).subscribe({
          next: data => {
            console.log("Información técnica registrada")
            this.formInfoTecnica.reset();
          },
          error: error => {
            console.log("Error registrando la información técnica", error)
            alert('Error registrando la información técnica')
          },
          complete: () => {
            this.router.navigate(['..'], {relativeTo: this.route})
          }
        })
    } else {
      this.infTecnicaService.editInfoTecnica(newInfoTecnica, this.indexInfoTec, candidatoId).subscribe({
        next: data => {
          console.log('Información técnica editada')
          this.formInfoTecnica.reset()
        },
        error: error => {
          console.log('Error editando la información técnica', error)
          alert('Error editando la información técnica')
        },
        complete: () => {
          this.router.navigate(['..'], {relativeTo: this.route})
        }
      })
    }
  }

  cancelarCreacion(){
    this.formInfoTecnica.reset()
  }
}


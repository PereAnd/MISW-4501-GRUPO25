import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { InfoAcademica } from 'src/app/candidates/models/info-academica';
import { InfoLaboral } from 'src/app/candidates/models/info-laboral';
import { InfAcademicaService } from 'src/app/candidates/services/inf-academica.service';
import { InfLaboralService } from 'src/app/candidates/services/inf-laboral.service';

@Component({
  selector: 'app-create-info-laboral',
  templateUrl: './create-info-laboral.component.html',
  styleUrls: ['./create-info-laboral.component.css']
})
export class CreateInfoLaboralComponent {

  indexInfoLab: number;
  candidatoId: number = 1;

  formInfoLaboral: FormGroup = new FormGroup({
    position: new FormControl('', Validators.required),
    organization: new FormControl('', Validators.required),
    activities: new FormControl('', Validators.required),
    dateFrom: new FormControl(null, Validators.required),
    dateTo: new FormControl(null, Validators.required)
  })

  get position() { return this.formInfoLaboral.get('position') }
  get organization() { return this.formInfoLaboral.get('organization') }
  get activities() { return this.formInfoLaboral.get('activities') }
  get dateFrom() { return this.formInfoLaboral.get('dateFrom') }
  get dateTo() { return this.formInfoLaboral.get('dateTo') }

  constructor(
    private infLaboralService: InfLaboralService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.indexInfoLab = this.route.snapshot.params['idia'];
    if(this.indexInfoLab){
      this.infLaboralService.findInfoLaboral(1, this.indexInfoLab)
      .subscribe({
        next: data => {
          this.formInfoLaboral.setValue({
            position: data.position,
            organization: data.organization,
            activities: data.activities,
            dateFrom: new Date(data.dateFrom),
            dateTo: new Date(data.dateTo)
          })
        },
        error: error => console.error('Error obteniendo la información laboral seleccionada', error)
      })
    }
  }

  registrarInfoLaboral(){
    const newInfoLaboral = new InfoLaboral(
      this.formInfoLaboral.value.position,
      this.formInfoLaboral.value.organization,
      this.formInfoLaboral.value.activities,
      this.formInfoLaboral.value.dateFrom,
      this.formInfoLaboral.value.dateTo,
      1 // OBTENER ID DEL CANDIDATO ACTUAL
    )

    this.infLaboralService.addInfoLaboral(newInfoLaboral, this.candidatoId).subscribe({
        next: data => {
          console.log("Información laboral registrada")
          this.formInfoLaboral.reset();
        },
        error: error => {
          console.log("Error registrando la información laboral", error)
          alert('Error registrando la información laboral')
        },
        complete: () => {
          this.router.navigate(['..'], {relativeTo: this.route})
        }
      })

  }

  cancelarCreacion(){
    this.formInfoLaboral.reset()
  }
}

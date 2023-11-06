import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { InfoLaboral } from 'src/app/candidates/models/info-laboral';
import { InfLaboralService } from 'src/app/candidates/services/inf-laboral.service';

@Component({
  selector: 'app-create-info-laboral',
  templateUrl: './create-info-laboral.component.html',
  styleUrls: ['./create-info-laboral.component.css']
})
export class CreateInfoLaboralComponent {

  indexInfoLab: number;
  candidatoId: number;
  isActualJob: boolean;

  formInfoLaboral: FormGroup = new FormGroup({
    position: new FormControl('', Validators.required),
    organization: new FormControl('', Validators.required),
    activities: new FormControl('', Validators.required),
    dateFrom: new FormControl(null, Validators.required),
    dateTo: new FormControl(null, Validators.required),
    actualJob: new FormControl(false, )
  })

  get position() { return this.formInfoLaboral.get('position') }
  get organization() { return this.formInfoLaboral.get('organization') }
  get activities() { return this.formInfoLaboral.get('activities') }
  get dateFrom() { return this.formInfoLaboral.get('dateFrom') }
  get dateTo() { return this.formInfoLaboral.get('dateTo') }
  get actualJob() { return this.formInfoLaboral.get('actualJob') }

  constructor(
    private infLaboralService: InfLaboralService,
    private router: Router,
    private route: ActivatedRoute
  ) {
    this.candidatoId = this.candidatoId = +localStorage.getItem('candidatoId')!;
  }

  ngOnInit(): void {
    this.isActualJob = false;
    this.indexInfoLab = this.route.snapshot.params['idil'];
    if(this.indexInfoLab){
      this.infLaboralService.findInfoLaboral(this.candidatoId, this.indexInfoLab)
      .subscribe({
        next: data => {
          this.formInfoLaboral.setValue({
            position: data.position,
            organization: data.organization,
            activities: data.activities,
            dateFrom: new Date(data.dateFrom),
            dateTo: data.dateTo ? new Date(data.dateTo) : null,
            actualJob: data.dateTo ? false : true
          })
          this.isActualJob = data.dateTo ? false : true;
        },
        error: error => console.error('Error obteniendo la información laboral seleccionada', error),
        complete: () => this.isActualJob ? this.formInfoLaboral.get('dateTo')?.disable() : this.formInfoLaboral.get('dateTo')?.enable()
      })
    }
  }

  registrarInfoLaboral(){

    const newInfoLaboral = new InfoLaboral(
      this.formInfoLaboral.value.position,
      this.formInfoLaboral.value.organization,
      this.formInfoLaboral.value.activities,
      this.formInfoLaboral.value.dateFrom,
      this.formInfoLaboral.value.dateTo ? this.formInfoLaboral.value.dateTo : null,
    )

    if(!this.indexInfoLab){
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
    } else {
      this.infLaboralService.editInfoLaboral(newInfoLaboral, this.indexInfoLab, this.candidatoId).subscribe({
        next: data => {
          console.log('Información laboral actualizada')
          this.formInfoLaboral.reset()
        },
        error: error => {
          console.log('Error editando la información laboral', error)
          alert('Error editando la información laboral')
        },
        complete: () => {
          this.router.navigate(['..'], {relativeTo: this.route})
        }
      })
    }

  }

  actualJobChange(){
    this.isActualJob = !this.isActualJob;
    this.isActualJob ? this.formInfoLaboral.get('dateTo')?.disable() : this.formInfoLaboral.get('dateTo')?.enable()
  }

  cancelarCreacion(){
    this.formInfoLaboral.reset()
  }


}

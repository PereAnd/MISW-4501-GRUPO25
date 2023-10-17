import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { InfoAcademica } from 'src/app/candidates/models/info-academica';
import { AddInfoAcademicaService } from 'src/app/candidates/services/add-info-academica.service';

@Component({
  selector: 'app-create-info-acad',
  templateUrl: './create-info-acad.component.html',
  styleUrls: ['./create-info-acad.component.css']
})
export class CreateInfoAcadComponent implements OnInit{

  indexInfoAcad: number;

  formInfoAcademica: FormGroup = new FormGroup({
    title: new FormControl('', Validators.required),
    institution: new FormControl('', Validators.required),
    beginDate: new FormControl(null, Validators.required),
    endDate: new FormControl(null, Validators.required),
    studyType: new FormControl('', Validators.required)
  })

  get title() { return this.formInfoAcademica.get('title') }
  get institution() { return this.formInfoAcademica.get('institution') }
  get beginDate() { return this.formInfoAcademica.get('beginDate') }
  get endDate() { return this.formInfoAcademica.get('endDate') }
  get studyType() { return this.formInfoAcademica.get('studyType') }

  constructor(
    private addInfoAcademicaService: AddInfoAcademicaService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.indexInfoAcad = this.route.snapshot.params['idia'];
    console.log('Entraste a la InfoAcad No. ', this.indexInfoAcad)
    if(this.indexInfoAcad){
      this.addInfoAcademicaService.findInfoAcademica(1, this.indexInfoAcad)
      .subscribe({
        next: data => {
          this.formInfoAcademica.setValue({
            title: data.tittle,
            institution: data.institution,
            beginDate: new Date(data.beginDate),
            endDate: new Date(data.endDate),
            studyType: data.studyType
          })
        },
        error: error => console.error('Error obteniendo la información académica seleccionada', error)
      })
    }
  }

  registrarInfoAcademica(){

    const newInfoAcademica = new InfoAcademica(
      this.formInfoAcademica.value.title,
      this.formInfoAcademica.value.institution,
      this.formInfoAcademica.value.beginDate,
      this.formInfoAcademica.value.endDate,
      this.formInfoAcademica.value.studyType,
      1 // OBTENER ID DEL CANDIDATO ACTUAL
    )

    if(!this.indexInfoAcad){
      this.addInfoAcademicaService.addInfoAcademica(newInfoAcademica).subscribe({
          next: data => {
            console.log("Información académica registrada", data)
            this.formInfoAcademica.reset();
          },
          error: error => {
            console.log("Error registrando la información académica", error)
            console.log(newInfoAcademica)
            alert('Error registrando la información académica')
          },
          complete: () => {
            this.router.navigate(['candidato/dashboard/1/list-info-academica'])
          }
        })
    } else {
      this.addInfoAcademicaService.editInfoAcademica(newInfoAcademica, this.indexInfoAcad).subscribe({
        next: data => {
          console.log('Información académica editada', data)
          this.formInfoAcademica.reset()
        },
        error: error => {
          console.log('Error editando la información académica', error)
          alert('Error editando la información académica')
        },
        complete: () => {
          this.router.navigate(['candidato/dashboard/1/list-info-academica'])
        }
      })
    }
  }

  cancelarCreacion(){
    this.formInfoAcademica.reset()
  }
}


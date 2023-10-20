import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { InfoAcademica } from 'src/app/candidates/models/info-academica';
import { InfAcademicaService } from 'src/app/candidates/services/inf-academica.service';

@Component({
  selector: 'app-create-info-acad',
  templateUrl: './create-info-acad.component.html',
  styleUrls: ['./create-info-acad.component.css']
})
export class CreateInfoAcadComponent implements OnInit{

  indexInfoAcad: number;
  candidatoId: number = 1;

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
    private infAcademicaService: InfAcademicaService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.indexInfoAcad = this.route.snapshot.params['idia'];
    if(this.indexInfoAcad){
      this.infAcademicaService.findInfoAcademica(1, this.indexInfoAcad)
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
      this.infAcademicaService.addInfoAcademica(newInfoAcademica, this.candidatoId).subscribe({
          next: data => {
            console.log("Información académica registrada", data)
            this.formInfoAcademica.reset();
          },
          error: error => {
            console.log("Error registrando la información académica", error)
            alert('Error registrando la información académica')
          },
          complete: () => {
            this.router.navigate(['..'], {relativeTo: this.route})
          }
        })
    } else {
      this.infAcademicaService.editInfoAcademica(newInfoAcademica, this.indexInfoAcad, this.candidatoId).subscribe({
        next: data => {
          console.log('Información académica editada')
          this.formInfoAcademica.reset()
        },
        error: error => {
          console.log('Error editando la información académica', error)
          alert('Error editando la información académica')
        },
        complete: () => {
          this.router.navigate(['..'], {relativeTo: this.route})
        }
      })
    }
  }

  cancelarCreacion(){
    this.formInfoAcademica.reset()
  }
}


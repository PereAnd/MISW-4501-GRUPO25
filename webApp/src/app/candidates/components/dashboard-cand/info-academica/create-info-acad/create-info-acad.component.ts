import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { InfoAcademica } from 'src/app/candidates/models/info-academica';
import { AddInfoAcademicaService } from 'src/app/candidates/services/add-info-academica.service';

@Component({
  selector: 'app-create-info-acad',
  templateUrl: './create-info-acad.component.html',
  styleUrls: ['./create-info-acad.component.css']
})
export class CreateInfoAcadComponent implements OnInit{

  formInfoAcademica: FormGroup;

  title: string;
  institution: string;
  beginDate: string;
  endDate: string;
  typeStudy: string;

  constructor(
    private formBuilder: FormBuilder,
    private addInfoAcademicaService: AddInfoAcademicaService
  ) { }

  ngOnInit(): void {
    this.formInfoAcademica = this.formBuilder.group({
      title: ['', Validators.required],
      institution: ['', Validators.required],
      beginDate: ['', Validators.required],
      endDate: ['', Validators.required],
      typeStudy: ['', Validators.required]
    })
  }

  registrarInfoAcademica(){
    this.title = this.formInfoAcademica.value.title;
    this.institution = this.formInfoAcademica.value.institution;
    this.beginDate = new Date(this.formInfoAcademica.value.beginDate).toISOString();
    this.endDate = new Date(this.formInfoAcademica.value.endDate).toISOString();
    this.typeStudy = this.formInfoAcademica.value.typeStudy;

    const newInfoAcademica = new InfoAcademica(
      this.formInfoAcademica.value.title,
      this.formInfoAcademica.value.institution,
      new Date(this.formInfoAcademica.value.beginDate).toISOString(),
      new Date(this.formInfoAcademica.value.endDate).toISOString(),
      this.formInfoAcademica.value.typeStudy,
      1 // OBTENER ID DEL CANDIDATO ACTUAL
    )

    this.addInfoAcademicaService.addInfoAcademica(newInfoAcademica)
      .subscribe({
        next: data => console.log("Información académica registrada", data),
        error: error => console.log("Error registrando la información académica", error)
      })
    this.formInfoAcademica.reset();
  }
}

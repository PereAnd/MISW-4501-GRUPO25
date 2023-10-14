import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

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
    private formBuilder: FormBuilder
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
    console.log("Registrar Info Academica");
  }
}

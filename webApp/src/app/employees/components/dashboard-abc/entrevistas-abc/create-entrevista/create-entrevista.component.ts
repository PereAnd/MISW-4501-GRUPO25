import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { RegCandidatoService } from 'src/app/candidates/services/reg-candidato.service';
import { Aplicacion } from 'src/app/companies/models/proyectos';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';
import { RegEmpresaService } from 'src/app/companies/services/reg-empresa.service';

@Component({
  selector: 'app-create-entrevista',
  templateUrl: './create-entrevista.component.html',
  styleUrls: ['./create-entrevista.component.css']
})
export class CreateEntrevistaComponent {
  title: string = '';
  empresaId: number;
  proyectoId: number;
  perfilId: number;
  application: any;
  isDone: boolean;

  formEntrevista: FormGroup = new FormGroup({
    enterviewDate: new FormControl('', [Validators.required]),
    enterviewTime: new FormControl('', [Validators.required]),
    done: new FormControl(false),
    feedback: new FormControl({value: '', disabled: true}, [Validators.required, Validators.maxLength(120)]),
  });

  get feedback() { return this.formEntrevista.get('feedback') }
  get done() { return this.formEntrevista.get('done') }
  get enterviewDate() { return this.formEntrevista.get('enterviewDate') }
  get enterviewTime() { return this.formEntrevista.get('enterviewTime') }

  constructor(
    private serviceProyectos: ProyectosService,
  ) { }

  ngOnInit(): void {
    this.serviceProyectos.getApplToInterview().subscribe({
      next: data => {
        if(data.entrevistas.length > 0){
          // this.formEntrevista.setValue({
          //   enterviewDate: new Date(data.entrevistas[0].enterviewDate),
          //   enterviewTime: data.entrevistas[0].enterviewDate.split('T')[1].split('.')[0],
          //   done: data.entrevistas[0].done,
          //   feedback: data.entrevistas[0].feedback
          // })
          this.formEntrevista.patchValue({
            enterviewDate: new Date(data.entrevistas[0].enterviewDate),
            enterviewTime: data.entrevistas[0].enterviewDate.split('T')[1].split('.')[0],
            done: data.entrevistas[0].done,
            feedback: data.entrevistas[0].feedback
          })
          if(data.entrevistas[0].done){
            this.formEntrevista.get('feedback')?.enable();
            this.isDone = true;
          } else {
            this.formEntrevista.get('feedback')?.disable();
            this.isDone = false;
          }
        }
      }
    })
  }

  interviewDone(){
    this.isDone = !this.isDone;
    this.isDone ? this.formEntrevista.get('feedback')?.enable() : this.formEntrevista.get('feedback')?.disable()
  }


  registrarEntrevista() {

    // this.perfilesService.getProfileToCompetencies().subscribe({
    //   next: data => { this.perfilId = data }
    // })
    // const newCompetencia = new Competencia(
    //   this.formEntrevista.value.name,
    //   this.formEntrevista.value.description
    // );
    // this.perfilesService.addCompetencia(this.empresaId, this.proyectoId, this.perfilId, newCompetencia, this.title).subscribe({
    //   next: data => {
    //     console.log(this.title + ' registrado');
    //   },
    //   error: error => console.error('Error registrando' + this.title, error)
    // })
  }

  cancelarCreacion() {
    this.formEntrevista.reset();
  }
}

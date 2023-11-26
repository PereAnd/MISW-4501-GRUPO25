import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';

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
    private proyectosService: ProyectosService,
    private perfilesService: PerfilesService
  ) { }

  ngOnInit(): void {
    this.proyectosService.getApplToInterview().subscribe({
      next: data => {
        this.application = data;
        if(data.entrevistas.length > 0){
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
    let fecha: Date = this.enterviewDate?.value;
    let interviewDate = fecha.toISOString().slice(0, 10) + 'T' + this.enterviewTime?.value;
    this.application.entrevistas.length > 0 ? interviewDate += '.000Z' : interviewDate += ':00.000Z'

    const newInterview = {
      enterviewDate: interviewDate,
      done: this.done?.value,
      feedback: this.feedback?.value
    }
    console.log('Entrevista a registrar', newInterview)
    if(this.application.entrevistas.length > 0){
      this.perfilesService.updateInterview(this.application, newInterview, this.application.entrevistas[0].id!).subscribe({
        next: data => {
          console.log('Entrevista actualizada');
        }, error: error => console.error('Error actualizando entrevista', error)
      })
    } else {
      this.perfilesService.addInterview(this.application, newInterview).subscribe({
        next: data => {
          console.log('Entrevista registrada');
        }, error: error => console.error('Error registrando entrevista', error)
      })
    }
  }

  cancelarCreacion() {
    this.formEntrevista.reset();
  }
}

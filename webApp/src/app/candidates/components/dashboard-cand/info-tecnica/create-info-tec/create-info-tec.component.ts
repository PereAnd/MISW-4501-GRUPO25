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
  formInfoTecnica: FormGroup = new FormGroup({
    type: new FormControl('', Validators.required),
    description: new FormControl('', Validators.required)
  })

  tiposInfoTecnica: string[] = ['Conocimiento', 'Habilidad']

  get type() { return this.formInfoTecnica.get('type') }
  get description() { return this.formInfoTecnica.get('description') }

  constructor(
    private infTecnicaService: InfTecnicaService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {

  }

  registrarInfoTecnica(){
    const newInfoTecnica = new InfoTecnica(
      this.formInfoTecnica.value.type,
      this.formInfoTecnica.value.description,
      1 // OBTENER ID DEL CANDIDATO ACTUAL
    )
      this.infTecnicaService.addInfoTecnica(newInfoTecnica).subscribe({
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

  }

  cancelarCreacion(){
    this.formInfoTecnica.reset()
  }
}

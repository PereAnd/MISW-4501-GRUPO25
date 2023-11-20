import { Component, Input } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Competencia } from 'src/app/companies/models/proyectos';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';

@Component({
  selector: 'app-create-competencia',
  templateUrl: './create-competencia.component.html',
  styleUrls: ['./create-competencia.component.css']
})
export class CreateCompetenciaComponent {
  title: string = '';
  empresaId: number;
  proyectoId: number;
  perfilId: number;

  formCompetencias: FormGroup = new FormGroup({
    name: new FormControl('', Validators.required),
    description: new FormControl('', [Validators.required, Validators.maxLength(90)]),
  });

  get name() { return this.formCompetencias.get('name') }
  get description() { return this.formCompetencias.get('description') }

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private perfilesService: PerfilesService
  ) { }

  ngOnInit(): void {
    this.empresaId = +localStorage.getItem('empresaId')!;
    this.perfilesService.getProjectToProfile().subscribe({
      next: data => { this.proyectoId = data }
    })
    this.perfilesService.getCompetenciaSelected().subscribe({
      next: data => {
        this.title = data;
      }
    })
  }

  registrarCompetencia() {
    this.perfilesService.getProfileToCompetencies().subscribe({
      next: data => { this.perfilId = data }
    })
    const newCompetencia = new Competencia(
      this.formCompetencias.value.name,
      this.formCompetencias.value.description
    );
    this.perfilesService.addCompetencia(this.empresaId, this.proyectoId, this.perfilId, newCompetencia, this.title).subscribe({
      next: data => {
        console.log(this.title + ' registrado');
      },
      error: error => console.error('Error registrando' + this.title, error)
    })
  }

  cancelarCreacion() {
    this.formCompetencias.reset();
  }
}

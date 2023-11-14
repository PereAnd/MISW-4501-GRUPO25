import { Component, Input } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Competencia } from 'src/app/companies/models/perfil';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';

@Component({
  selector: 'app-create-competencia',
  templateUrl: './create-competencia.component.html',
  styleUrls: ['./create-competencia.component.css']
})
export class CreateCompetenciaComponent {
  title: string = '';

  formCompetencias: FormGroup = new FormGroup({
    name: new FormControl('', Validators.required),
    description: new FormControl('', [Validators.required, Validators.maxLength(50)]),
  });

  get name() { return this.formCompetencias.get('name') }
  get description() { return this.formCompetencias.get('description') }

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private perfilesService: PerfilesService
  ) { }

  ngOnInit(): void {
    this.perfilesService.getCompetenciaSelected().subscribe({
      next: data => {
        this.title = data;
      }
    })
  }

  registrarCompetencia() {
    const newCompetencia = new Competencia(
      this.formCompetencias.value.name,
      this.formCompetencias.value.description
    );
    if (this.title == 'Conocimiento') this.perfilesService.addConocimientoTemp(newCompetencia);
    if (this.title == 'Habilidad') this.perfilesService.addHabilidadeTemp(newCompetencia);
    if (this.title == 'Idioma') this.perfilesService.addIdiomaTemp(newCompetencia);
  }

  cancelarCreacion() {
    this.formCompetencias.reset();
  }
}

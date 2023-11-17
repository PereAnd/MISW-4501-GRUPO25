import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { Proyecto } from 'src/app/companies/models/proyecto';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';

@Component({
  selector: 'app-create-proyecto',
  templateUrl: './create-proyecto.component.html',
  styleUrls: ['./create-proyecto.component.css'],
})
export class CreateProyectoComponent {
  indexProyecto: number;
  empresaId: number;

  formProyectos: FormGroup = new FormGroup({
  proyecto: new FormControl('', Validators.required),
  description: new FormControl('', Validators.required),
  });

  get proyecto() { return this.formProyectos.get('proyecto') }
  get description() { return this.formProyectos.get('description') }

  constructor(
    private proyectosService: ProyectosService,
    private router: Router,
    private route: ActivatedRoute,
    private perfilesService: PerfilesService
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    this.indexProyecto = this.route.snapshot.params['idp'];
    this.perfilesService.setProjectToProfile(this.indexProyecto)
    if (this.indexProyecto) {
      this.proyectosService.findProyecto(this.empresaId, this.indexProyecto).subscribe({
        next: (data) => {
          this.formProyectos.setValue({
            proyecto: data.proyecto,
            description: data.description,
          });
        },
        error: (error) =>
          console.error('Error obteniendo el proyecto seleccionado', error),
      });
    }
  }

  registrarProyecto() {
    const newProyecto = new Proyecto(
      this.formProyectos.value.proyecto,
      this.formProyectos.value.description,
      this.empresaId
    );
    if (!this.indexProyecto) {
      this.proyectosService.addProyecto(newProyecto, this.empresaId).subscribe({
        next: (data) => {
          console.log('Proyecto registrado');
          this.router.navigate(['../', data.id], { relativeTo: this.route });
        },
        error: (error) => {
          console.log('Error registrando el proyecto', error);
          alert('Error registrando el proyecto');
        },
      });
    } else {
      this.proyectosService
        .editProyecto(newProyecto, this.indexProyecto, this.empresaId)
        .subscribe({
          next: (data) => {
            console.log('Proyecto actualizado');
          },
          error: (error) => {
            console.log('Error editando el proyecto', error);
            alert('Error editando el proyecto');
          },
        });
    }
  }

  cancelarCreacion() {
    this.formProyectos.reset();
    this.router.navigate(['..'], { relativeTo: this.route });
  }
}

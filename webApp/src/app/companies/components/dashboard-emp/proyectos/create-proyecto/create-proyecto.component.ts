import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { Proyecto } from 'src/app/companies/models/proyecto';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';

@Component({
  selector: 'app-create-proyecto',
  templateUrl: './create-proyecto.component.html',
  styleUrls: ['./create-proyecto.component.css'],
})
export class CreateProyectoComponent {
  indexProyecto: number;

  formProyectos: FormGroup = new FormGroup({
    proyecto: new FormControl('', Validators.required),
    description: new FormControl('', Validators.required),
  });

  get proyecto() {
    return this.formProyectos.get('proyecto');
  }
  get description() {
    return this.formProyectos.get('description');
  }

  constructor(
    private proyectosService: ProyectosService,
    private router: Router,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.indexProyecto = this.route.snapshot.params['idp'];
    if (this.indexProyecto) {
      this.proyectosService.findProyecto(1, this.indexProyecto).subscribe({
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
    const empresaId: number = 1;
    const newProyecto = new Proyecto(
      this.formProyectos.value.proyecto,
      this.formProyectos.value.description,
      1 // OBTENER ID DEL CANDIDATO ACTUAL
    );
    if (!this.indexProyecto) {
      this.proyectosService.addProyecto(newProyecto, empresaId).subscribe({
        next: (data) => {
          console.log('Proyecto registrado');
          this.formProyectos.reset();
        },
        error: (error) => {
          console.log('Error registrando el proyecto', error);
          alert('Error registrando el proyecto');
        },
        complete: () => {
          this.router.navigate(['..'], { relativeTo: this.route });
        },
      });
    } else {
      this.proyectosService
        .editProyecto(newProyecto, this.indexProyecto, empresaId)
        .subscribe({
          next: (data) => {
            console.log('Proyecto actualizado');
            this.formProyectos.reset();
          },
          error: (error) => {
            console.log('Error editando el proyecto', error);
            alert('Error editando el proyecto');
          },
          complete: () => {
            this.router.navigate(['..'], { relativeTo: this.route });
          },
        });
    }
  }

  cancelarCreacion() {
    this.formProyectos.reset();
  }
}

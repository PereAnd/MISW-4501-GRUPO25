import { Component, OnInit, ViewChild } from '@angular/core';
import { MatAccordion } from '@angular/material/expansion';
import { forkJoin } from 'rxjs';
import { Perfil, Proyecto } from 'src/app/companies/models/proyectos';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';

@Component({
  selector: 'app-entrevistas-emp',
  templateUrl: './entrevistas-emp.component.html',
  styleUrls: ['./entrevistas-emp.component.css'],
})
export class EntrevistasEmpComponent implements OnInit {
  @ViewChild(MatAccordion) accordion: MatAccordion;

  projects: any[] = [{project: {}, profiles: []}];
  empresaId: number;

  constructor(
    private proyectosService: ProyectosService,
    private perfilesService: PerfilesService
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    this.getProjectsaAndProfiles();
  }
  getProjectsaAndProfiles(){
    this.proyectosService.listProyectos(this.empresaId).subscribe({
      next: (projects: any) => {
        const perfilesRequests = projects.map((project: Proyecto) =>
          this.perfilesService.listPerfiles(this.empresaId, project.id!)
        );
        forkJoin(perfilesRequests).subscribe({
          next: (profilesForProject: any) => {
            this.projects = projects.map((project: Proyecto, index: number) => ({
              project,
              profiles: profilesForProject[index],
            }));
          },
          error: (error) => {
            console.error('Error al obtener perfiles:', error);
          }, complete: () => {
            console.log(this.projects)
          }
        })
      }, error: error => {
        console.error('Error al obtener proyectos:', error)
      }
    })
  }
}

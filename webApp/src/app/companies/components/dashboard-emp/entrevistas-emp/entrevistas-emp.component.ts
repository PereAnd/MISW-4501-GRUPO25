import { Component, OnInit, ViewChild } from '@angular/core';
import { MatAccordion } from '@angular/material/expansion';
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
  projects: Proyecto[] = []; // name, description, id
  profiles: Perfil[] = [];
  empresaId: number;

  constructor(
    private proyectosService: ProyectosService,
    private perfilesService: PerfilesService
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    this.proyectosService.listProyectos(this.empresaId).subscribe({
      next: (data) => {
        this.projects = data;
        data.forEach((project: { id: number; }) => {
          this.perfilesService
            .listPerfiles(this.empresaId, project.id!)
            .subscribe({
              next: (data) => {
                this.profiles.push(...data);
              },
              error: (error) => {
                console.error('Error obteniendo los perfiles', error);
              },
            });
        });
      },
      error: (error) => {
        console.error('Error obteniendo los proyectos', error);
      }, complete: () => {
        console.log(this.projects);
        console.log(this.profiles);
      }
    });
  }

  getProfiles(projects: Proyecto[]) {
    this.profiles = [];
    projects.forEach((project) => {
      this.perfilesService.listPerfiles(this.empresaId, project.id!).subscribe({
        next: (data) => {
          this.profiles.push(...data);
        },
        error: (error) => {
          console.error('Error obteniendo los perfiles', error);
        },
      });
    });
  }
}

import { Component, OnInit } from '@angular/core';
import { Perfil } from 'src/app/companies/models/proyectos';
import { Proyecto } from 'src/app/companies/models/proyectos';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';

@Component({
  selector: 'app-detail-proyecto',
  templateUrl: './detail-proyecto.component.html',
  styleUrls: ['./detail-proyecto.component.css']
})
export class DetailProyectoComponent implements OnInit{

  projectDetail: Proyecto;
  perfilesProject: Perfil[];

  constructor(
    private proyectosService: ProyectosService
  ){}

  ngOnInit(): void {
    this.proyectosService.getProjectDetail().subscribe({
      next: project => {
        this.projectDetail = project;
      }
    })
  }
}

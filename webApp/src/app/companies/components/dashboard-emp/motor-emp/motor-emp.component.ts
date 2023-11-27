import { Component, OnInit, ViewChild } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { MatAccordion } from '@angular/material/expansion';
import { Candidato } from 'src/app/candidates/models/candidato';
import { RegCandidatoService } from 'src/app/candidates/services/reg-candidato.service';
import { Aplicacion, Perfil, Proyecto } from 'src/app/companies/models/proyectos';
import { BusquedaService } from 'src/app/companies/services/busqueda.service';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';

@Component({
  selector: 'app-motor-emp',
  templateUrl: './motor-emp.component.html',
  styleUrls: ['./motor-emp.component.css']
})
export class MotorEmpComponent implements OnInit{
  @ViewChild(MatAccordion) accordion: MatAccordion;
  panelOpenState = false;

  empresaId: number;
  projectId: number;
  profileId: number;

  projects: Proyecto[] = [];
  profiles: Perfil[] = [];

  searchId: number;
  matchesCandidates: any[] = [];

  aplicaciones: any[] = [];
  msgNotFound: string = 'No hay resultados';

  constructor(
    private busquedaService: BusquedaService,
    private proyectosService: ProyectosService,
    private perfilesService: PerfilesService,
    private candidatosService: RegCandidatoService
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    this.proyectosService.listProyectos(this.empresaId).subscribe({
      next: listProjects => {
        this.projects = listProjects;
      }
    })
    this.perfilesService.listAplicacionesEmpresa(this.empresaId).subscribe({
      next: listAplicaciones => {
        listAplicaciones.forEach(aplicacion => {
          this.aplicaciones.push(aplicacion.candidatoId)
        })
      }
    })
  }

  formBusqueda: FormGroup = new FormGroup({
    project: new FormControl('', Validators.required),
    profile: new FormControl('', Validators.required)
  })

  get project() { return this.formBusqueda.get('project') }
  get profile() { return this.formBusqueda.get('profile') }

  buscar(){
    this.projectId = this.formBusqueda.value.project;
    this.profileId = this.formBusqueda.value.profile;
    console.log('Buscando...', 'Proyecto: ', this.projectId, 'Perfil: ', this.profileId);
    this.busquedaService.searchCandidates(this.empresaId, this.projectId, this.profileId).subscribe({
      next: response => {
        this.searchId = response.id;
      }
    })
  }
  updateProfiles(projectId: number){
    this.perfilesService.listPerfiles(this.empresaId, projectId).subscribe({
      next: listProfiles => {
        this.profiles = listProfiles;
      }
    })
  }
  // TODO: Funcion provisional para terminar busqueda
  // provisionalKillSearch(){
  //   this.busquedaService.provisionalKillSearch(this.empresaId, this.projectId, this.profileId, this.searchId).subscribe({
  //     next: response => {
  //       console.log(response);
  //     }
  //   })
  // }

  getSearchResults(){
    this.busquedaService.getSearchResults(this.empresaId, this.projectId, this.profileId, this.searchId).subscribe({
      next: response => {
        if(response.resultados.length == 0){
          this.msgNotFound = 'No hay resultados para esta búsqueda'
        } else {
          response.resultados.map( (result: any) => {
            this.candidatosService.getDatosCandidato(result.candidatoId).subscribe({
              next: candidato => {
                this.matchesCandidates.push(candidato);
              }
            })
          })
        }
      }
    })
  }

  solicitarEntrevista(candidateId: number){
    const aplicacion: Aplicacion = {
      'applicationDate': new Date().toISOString(),
      'status': 'Entrevista no programada',
      'candidatoId': candidateId,
      'result': 'En entrevistas'
    }
    this.perfilesService.addAplicacionCand(this.empresaId, this.projectId, this.profileId, aplicacion).subscribe({
      next: response => {
        console.log('Entrevista solicitada');
        this.perfilesService.listAplicacionesEmpresa(this.empresaId).subscribe({
          next: listAplicaciones => {
            listAplicaciones.forEach(aplicacion => {
              this.aplicaciones.push(aplicacion.candidatoId)
            })
          }
        })
      }
    })
  }
}

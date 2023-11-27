import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators, NgModel } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { Candidato } from 'src/app/candidates/models/candidato';
import { RegCandidatoService } from 'src/app/candidates/services/reg-candidato.service';
import { Aplicacion, Competencia } from 'src/app/companies/models/proyectos';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';

@Component({
  selector: 'app-create-appl',
  templateUrl: './create-appl.component.html',
  styleUrls: ['./create-appl.component.css']
})
export class CreateApplComponent {
  title: string = '';
  empresaId: number;

  profiles: any[] = [];
  projects: any[] = [];
  aplicaciones: any[] = [];
  projectId: number;
  profileId: number;
  candidato: Candidato;

  formAsignacion: FormGroup = new FormGroup({
    project: new FormControl('', Validators.required),
    profile: new FormControl('', Validators.required),
  });

  get project() { return this.formAsignacion.get('project') }
  get profile() { return this.formAsignacion.get('profile') }

  constructor(
    private proyectosService: ProyectosService,
    private perfilesService: PerfilesService,
    private candidatosService: RegCandidatoService
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    this.candidato = this.candidatosService.getCandidateForDetail();
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

  solicitarEntrevista(candidateId: number){
    const aplicacion: Aplicacion = {
      'applicationDate': new Date().toISOString(),
      'status': 'Entrevista no programada',
      'candidatoId': candidateId,
      'result': 'En entrevistas'
    }
    this.projectId = this.formAsignacion.get('project')?.value;
    this.profileId = this.formAsignacion.get('profile')?.value;

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

  updateProfiles(projectId: number){
    this.perfilesService.listPerfiles(this.empresaId, projectId).subscribe({
      next: listProfiles => {
        this.profiles = listProfiles;
      }
    })
  }

  cancelarCreacion() {
    this.formAsignacion.reset();
  }
}

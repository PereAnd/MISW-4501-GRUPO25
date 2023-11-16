import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Competencia, Perfil } from '../models/perfil';

@Injectable({
  providedIn: 'root'
})
export class PerfilesService {

  profileDetail: Perfil;
  competenciaSelected: string = '';
  projectToProfile: number;
  profileToCompetencies: number;

  constructor(
    private httpClient: HttpClient
  ) { }

  // Tipo de competencia seleccionada (conocimiento, habilidad, idioma)
  setCompetenciaSelected(tipo: string){
    this.competenciaSelected = tipo;
  }
  getCompetenciaSelected(): Observable<string>{
    return new Observable<string>(observer => {
      observer.next(this.competenciaSelected)
    });
  }

  // Perfil seleccionado para ver detalle
  setProfileDetail(profile: Perfil){
    this.profileDetail = profile;
  }
  getProfileDetail(): Observable<Perfil>{
    return new Observable<Perfil>(observer => {
      observer.next(this.profileDetail)
    });
  }

  // Proyecto seleccionado para agregar perfil
  setProjectToProfile(projectId: number){
    this.projectToProfile = projectId;
  }
  getProjectToProfile(): Observable<number>{
    return new Observable<number>(observer => {
      observer.next(this.projectToProfile)
    });
  }

  // Perfil seleccionado para agregar competencias
  setProfileToCompetencies(profileId: number){
    this.profileToCompetencies = profileId;
  }
  getProfileToCompetencies(): Observable<number>{
    return new Observable<number>(observer => {
      observer.next(this.profileToCompetencies)
    });
  }

  // Servicios
  listPerfiles(idEmpresa: number, idProyecto: number): Observable<any>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + idEmpresa + '/proyecto/' + idProyecto + '/perfil';
    return this.httpClient.get<any>(baseUrl);
  }

  findPerfil(idEmpresa: number, idProyecto: number, idPerfil: number): Observable<Perfil>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + idEmpresa + '/proyecto/' + idProyecto + '/perfil/' + idPerfil;
    return this.httpClient.get<Perfil>(baseUrl);
  }

  addPerfil(proyectoId: number, empresaId: number, perfil: Perfil): Observable<Perfil>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + empresaId + '/proyecto/' + proyectoId + '/perfil';
    return this.httpClient.post<Perfil>(baseUrl, perfil);
  }

  editPerfil(proyectoId: number, empresaId: number, perfilId: number, perfil: Perfil): Observable<Perfil>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + empresaId + '/proyecto/' + proyectoId + '/perfil/' + perfilId;
    return this.httpClient.patch<Perfil>(baseUrl, perfil);
  }

  deletePerfil(empresaId: number, proyectoId: number, perfilId: number): Observable<string>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + empresaId + '/proyecto/' + proyectoId + '/perfil/' + perfilId;
    return this.httpClient.delete<string>(baseUrl);
  }

  addCompetencia(empresaId: number, proyectoId: number, perfilId: number, competencia: Competencia, tipo: string): Observable<Competencia>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + empresaId + '/proyecto/' + proyectoId + '/perfil/' + perfilId
    if (tipo == 'Conocimiento') baseUrl += '/conocimiento';
    else if (tipo == 'Habilidad') baseUrl += '/habilidad';
    else if (tipo == 'Idioma') baseUrl += '/idioma';
    return this.httpClient.post<Competencia>(baseUrl, competencia);
  }

  getConocimientos(empresaId: number, proyectoId: number, perfilId: number): Observable<Competencia[]>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + empresaId + '/proyecto/' + proyectoId + '/perfil/' + perfilId + '/conocimiento';
    return this.httpClient.get<Competencia[]>(baseUrl);
  }

  getHabilidades(empresaId: number, proyectoId: number, perfilId: number): Observable<Competencia[]>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + empresaId + '/proyecto/' + proyectoId + '/perfil/' + perfilId + '/habilidad';
    return this.httpClient.get<Competencia[]>(baseUrl);
  }

  getIdiomas(empresaId: number, proyectoId: number, perfilId: number): Observable<Competencia[]>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + empresaId + '/proyecto/' + proyectoId + '/perfil/' + perfilId + '/idioma';
    return this.httpClient.get<Competencia[]>(baseUrl);
  }
}

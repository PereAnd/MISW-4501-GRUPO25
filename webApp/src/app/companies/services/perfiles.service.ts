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
  conocimientosTemp: Competencia[] = [];
  habilidadesTemp: Competencia[] = [];
  idiomasTemp: Competencia[] = [];

  constructor(
    private httpClient: HttpClient
  ) { }

  setCompetenciaSelected(tipo: string){
    this.competenciaSelected = tipo;
  }

  getCompetenciaSelected(): Observable<string>{
    return new Observable<string>(observer => {
      observer.next(this.competenciaSelected)
    });
  }

  setProfileDetail(profile: Perfil){
    this.profileDetail = profile;
  }

  getProfileDetail(): Observable<Perfil>{
    return new Observable<Perfil>(observer => {
      observer.next(this.profileDetail)
    });
  }

  addConocimientoTemp(conocimiento: Competencia){
    this.conocimientosTemp.push(conocimiento);
  }

  getConocimientosTemp(): Observable<Competencia[]>{
    return new Observable<Competencia[]>(observer => {
      observer.next(this.conocimientosTemp)
    });
  }

  addHabilidadeTemp(habilidad: Competencia){
    this.habilidadesTemp.push(habilidad);
  }

  getHabilidadesTemp(): Observable<Competencia[]>{
    return new Observable<Competencia[]>(observer => {
      observer.next(this.habilidadesTemp)
    });
  }

  addIdiomaTemp(idioma: Competencia){
    this.idiomasTemp.push(idioma);
  }

  getIdiomasTemp(): Observable<Competencia[]>{
    return new Observable<Competencia[]>(observer => {
      observer.next(this.idiomasTemp)
    });
  }

  listPerfiles(idEmpresa: number, idProyecto: number): Observable<any>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + idEmpresa + '/proyecto/' + idProyecto + '/perfil';
    return this.httpClient.get<any>(baseUrl);
  }

  addPerfil(proyectoId: number, empresaId: number, perfil: Perfil): Observable<Perfil>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + empresaId + '/proyecto/' + proyectoId + '/perfil';
    return this.httpClient.post<Perfil>(baseUrl, perfil);
  }
}

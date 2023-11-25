import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Aplicacion, Proyecto } from '../models/proyectos';

@Injectable({
  providedIn: 'root'
})
export class ProyectosService {

  projectDetail: Proyecto;
  applInterview: Aplicacion;

  constructor(
    private httpClient: HttpClient
  ) { }

  setApplToInterview(application: any){
    this.applInterview = application;
  }

  getApplToInterview(): Observable<any>{
    return new Observable<any>(observer => {
      observer.next(this.applInterview)
    });
  }

  setProjectDetail(project: Proyecto){
    this.projectDetail = project;
  }

  getProjectDetail(): Observable<Proyecto>{
    return new Observable<Proyecto>(observer => {
      observer.next(this.projectDetail)
    });
  }

  listProyectos(empresaId: number): Observable<any>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/proyecto';
    return this.httpClient.get<Proyecto>(baseUrl);
  }

  addProyecto(proyecto: Proyecto, empresaId: number): Observable<Proyecto>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/proyecto';
    return this.httpClient.post<Proyecto>(baseUrl, proyecto);
  }

  findProyecto(empresaId: number, indexProyecto: number): Observable<Proyecto>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/proyecto/' + indexProyecto;
    return this.httpClient.get<Proyecto>(baseUrl);
  }

  editProyecto(proyecto: Proyecto, indexProyecto: number, empresaId: number):Observable<Proyecto>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/proyecto/' + indexProyecto;
    return this.httpClient.patch<Proyecto>(baseUrl, proyecto);
  }
}

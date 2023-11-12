import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Perfil } from '../models/perfil';

@Injectable({
  providedIn: 'root'
})
export class PerfilesService {

  profileDetail: Perfil;

  constructor(
    private httpClient: HttpClient
  ) { }

  setProfileDetail(profile: Perfil){
    this.profileDetail = profile;
  }

  getProfileDetail(): Observable<Perfil>{
    return new Observable<Perfil>(observer => {
      observer.next(this.profileDetail)
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

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Perfil } from '../models/perfil';

@Injectable({
  providedIn: 'root'
})
export class PerfilesService {

  constructor(
    private httpClient: HttpClient
  ) { }

  listPerfiles(idEmpresa: number, idProyecto: number): Observable<any>{
    let baseUrl: string = environment.HOST_PERF + 'empresa/' + idEmpresa + '/proyecto/' + idProyecto + '/perfil';
    return this.httpClient.get<any>(baseUrl);
  }
}

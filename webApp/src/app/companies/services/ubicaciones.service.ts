import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Ubicacion } from '../models/empresas';

@Injectable({
  providedIn: 'root'
})
export class UbicacionesService {

  constructor(
    private httpClient: HttpClient
  ) { }

  listUbicaciones(idEmpresa: number): Observable<any>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + idEmpresa + '/ubicacion';
    return this.httpClient.get<Ubicacion>(baseUrl);
  }
  addUbicacion(ubicacion: Ubicacion, empresaId: number): Observable<Ubicacion>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/ubicacion';
    return this.httpClient.post<Ubicacion>(baseUrl, ubicacion);
  }

  findUbicacion(empresaId: number, indexUbicacion: number): Observable<Ubicacion>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/ubicacion/' + indexUbicacion;
    return this.httpClient.get<Ubicacion>(baseUrl);
  }

  editUbicacion(ubicacion: Ubicacion, indexUbicacion: number, empresaId: number):Observable<Ubicacion>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/ubicacion/' + indexUbicacion;
    return this.httpClient.patch<Ubicacion>(baseUrl, ubicacion);
  }
}

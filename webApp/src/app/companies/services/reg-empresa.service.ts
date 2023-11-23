import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Empresa, Ubicacion, Vertical } from '../models/empresas';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class RegEmpresaService {

  constructor(
    private httpClient: HttpClient
  ) { }

  registrarEmpresa(empresa: Empresa): Observable<Empresa> {
    let baseUrl: string = environment.HOST_EMP + 'empresa'
    return this.httpClient.post<Empresa>(baseUrl, empresa)
  }

  getDatosEmpresa(idEmpresa: number): Observable<Empresa> {
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + idEmpresa;
    return this.httpClient.get<Empresa>(baseUrl);
  }

  updateDatosEmpresa(empresa: Empresa): Observable<Empresa> {
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresa.id;
    return this.httpClient.patch<Empresa>(baseUrl, empresa)
  }

  listVerticales(empresaId: number): Observable<any>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/vertical';
    return this.httpClient.get<Vertical>(baseUrl);
  }

  addVertical(vertical: Vertical, empresaId: number): Observable<Vertical>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/vertical';
    return this.httpClient.post<Vertical>(baseUrl, vertical);
  }

  findVertical(empresaId: number, indexVertical: number): Observable<Vertical>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/vertical/' + indexVertical;
    return this.httpClient.get<Vertical>(baseUrl);
  }

  editVertical(vertical: Vertical, indexVertical: number, empresaId: number):Observable<Vertical>{
    let baseUrl: string = environment.HOST_EMP + 'empresa/' + empresaId + '/vertical/' + indexVertical;
    return this.httpClient.patch<Vertical>(baseUrl, vertical);
  }

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

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Empresa } from '../models/empresa';
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
}

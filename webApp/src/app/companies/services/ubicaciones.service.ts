import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Ubicacion } from '../models/ubicacion';

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
}

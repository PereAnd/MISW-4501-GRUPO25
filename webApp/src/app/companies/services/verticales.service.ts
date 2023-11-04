import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Vertical } from '../models/vertical';

@Injectable({
  providedIn: 'root'
})
export class VerticalesService {

  constructor(
    private httpClient: HttpClient
  ) { }

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
}

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class InfLaboralService {

  constructor(
    private httpClient: HttpClient
  ) { }

  listInfoLaboral(idCandidato: number): Observable<any>{
    let baseUrl: string = environment.HOST + 'candidato/' + idCandidato + '/informacionLaboral';
    return this.httpClient.get<any>(baseUrl);
  }
}

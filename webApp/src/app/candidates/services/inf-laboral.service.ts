import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { InfoLaboral } from '../models/info-laboral';

@Injectable({
  providedIn: 'root'
})
export class InfLaboralService {

  constructor(
    private httpClient: HttpClient
  ) { }

  listInfoLaboral(idCandidato: number): Observable<any>{
    let baseUrl: string = environment.HOST_CAND + 'candidato/' + idCandidato + '/informacionLaboral';
    return this.httpClient.get<any>(baseUrl);
  }

  addInfoLaboral(infoLaboral: InfoLaboral, candidatoId: number): Observable<InfoLaboral>{
    let baseUrl: string = environment.HOST_CAND + 'candidato/' + candidatoId + '/informacionLaboral';
    return this.httpClient.post<InfoLaboral>(baseUrl, infoLaboral);
  }

  findInfoLaboral(indexCandidato: number, indexInfoLab: number): Observable<InfoLaboral>{
    let baseUrl: string = environment.HOST_CAND + 'candidato/' + indexCandidato + '/informacionLaboral/' + indexInfoLab;
    return this.httpClient.get<InfoLaboral>(baseUrl);
  }

  editInfoLaboral(infoLaboral: InfoLaboral, indexInfoLaboral: number, candidatoId: number):Observable<InfoLaboral>{
    let baseUrl: string = environment.HOST_CAND + 'candidato/' + candidatoId + '/informacionLaboral/' + indexInfoLaboral;
    return this.httpClient.patch<InfoLaboral>(baseUrl, infoLaboral);
  }
}

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { InfoAcademica } from '../models/info-academica';

@Injectable({
  providedIn: 'root'
})
export class InfAcademicaService {

  constructor(
    private httpClient: HttpClient
  ) { }

  listInfoAcademica(idCandidato: number): Observable<any>{
    let baseUrl: string = environment.HOST_CAND + 'candidato/' + idCandidato + '/informacionAcademica';
    return this.httpClient.get<any>(baseUrl);
  }

  addInfoAcademica(infoAcademica: InfoAcademica, candidatoId: number): Observable<InfoAcademica>{
    let baseUrl: string = environment.HOST_CAND + 'candidato/' + candidatoId + '/informacionAcademica';
    return this.httpClient.post<InfoAcademica>(baseUrl, infoAcademica);
  }

  findInfoAcademica(indexCandidato: number, indexInfoAcad: number): Observable<InfoAcademica>{
    let baseUrl: string = environment.HOST_CAND + 'candidato/' + indexCandidato + '/informacionAcademica/' + indexInfoAcad;
    return this.httpClient.get<InfoAcademica>(baseUrl);
  }

  editInfoAcademica(infoAcademica: InfoAcademica, indexInfoAcad: number, candidatoId: number):Observable<InfoAcademica>{
    let baseUrl: string = environment.HOST_CAND + 'candidato/' + candidatoId + '/informacionAcademica/' + indexInfoAcad;
    return this.httpClient.patch<InfoAcademica>(baseUrl, infoAcademica);
  }
}

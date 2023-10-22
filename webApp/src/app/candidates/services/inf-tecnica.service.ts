import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { InfoTecnica } from '../models/info-tecnica';

@Injectable({
  providedIn: 'root'
})
export class InfTecnicaService {

  constructor(
    private httpClient: HttpClient
  ) { }

  listInfoTecnica(idCandidato: number): Observable<any>{
    let baseUrl: string = environment.HOST + 'candidato/' + idCandidato + '/informacionTecnica';
    return this.httpClient.get<any>(baseUrl);
  }
  addInfoTecnica(infoTecnica: InfoTecnica, candidatoId: number): Observable<InfoTecnica>{
    let baseUrl: string = environment.HOST + 'candidato/' + candidatoId + '/informacionTecnica';
    return this.httpClient.post<InfoTecnica>(baseUrl, infoTecnica);
  }

  findInfoTecnica(indexCandidato: number, indexInfoTec: number): Observable<InfoTecnica>{
    let baseUrl: string = environment.HOST + 'candidato/' + indexCandidato + '/informacionTecnica/' + indexInfoTec;
    return this.httpClient.get<InfoTecnica>(baseUrl);
  }

  editInfoTecnica(infoTecnica: InfoTecnica, indexInfoTec: number, candidatoId: number):Observable<InfoTecnica>{
    let baseUrl: string = environment.HOST + 'candidato/' + candidatoId + '/informacionTecnica/' + indexInfoTec;
    return this.httpClient.patch<InfoTecnica>(baseUrl, infoTecnica);
  }
}

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { InfoAcademica } from '../models/info-academica';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class AddInfoAcademicaService {

  constructor(
    private httpClient: HttpClient
  ) { }

  addInfoAcademica(infoAcademica: InfoAcademica): Observable<InfoAcademica>{
    console.log(infoAcademica)
    let baseUrl: string = environment.HOST + 'candidato/' + infoAcademica.candidatoId + '/informacionAcademica';
    return this.httpClient.post<InfoAcademica>(baseUrl, infoAcademica);
  }

  findInfoAcademica(indexCandidato: number, indexInfoAcad: number): Observable<InfoAcademica>{
    let baseUrl: string = environment.HOST + 'candidato/' + indexCandidato + '/informacionAcademica/' + indexInfoAcad;
    return this.httpClient.get<InfoAcademica>(baseUrl);
  }

  editInfoAcademica(infoAcademica: InfoAcademica, indexInfoAcad: number):Observable<InfoAcademica>{
    let baseUrl: string = environment.HOST + 'candidato/' + infoAcademica.candidatoId + '/informacionAcademica/' + indexInfoAcad;
    return this.httpClient.patch<InfoAcademica>(baseUrl, infoAcademica);
  }
}

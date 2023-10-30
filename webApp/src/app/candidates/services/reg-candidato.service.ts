import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Candidato } from '../models/candidato';

import { environment } from '../../../environments/environment.development'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RegCandidatoService {

  constructor(
    private httpClient: HttpClient
  ) { }

  registrarCandidato(candidato: Candidato): Observable<Candidato> {
    let baseUrl: string = environment.HOST_CAND + 'candidato';
    return this.httpClient.post<Candidato>(baseUrl, candidato);
  }

  getDatosCandidato(idCandidato: number): Observable<Candidato> {
    let baseUrl: string = environment.HOST_CAND + 'candidato/' + idCandidato;
    return this.httpClient.get<Candidato>(baseUrl);
  }

  updateDatosCandidato(candidato: Candidato): Observable<Candidato> {
    let baseUrl: string = environment.HOST_CAND + 'candidato/' + candidato.id;
    console.log('Candidato:', candidato)
    console.log('URL:', baseUrl)
    console.log('birthDate:', candidato.birthDate?.toISOString())
    return this.httpClient.patch<Candidato>(baseUrl, candidato)
  }
}

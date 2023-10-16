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
    return this.httpClient.post<Candidato>(environment.URL_REGISTRO_CANDIDATOS, candidato);
  }
}

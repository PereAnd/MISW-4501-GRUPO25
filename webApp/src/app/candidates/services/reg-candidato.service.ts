import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Candidato } from '../models/candidato';

import { environment } from '../../../environments/environment.development'

@Injectable({
  providedIn: 'root'
})
export class RegCandidatoService {

  constructor(
    private httpClient: HttpClient
  ) { }

  agregarCandidato(candidato: Candidato){
    console.log(candidato)
    this.httpClient.post(environment.URL_REGISTRO_CANDIDATOS, candidato)
      .subscribe({
        next: data => console.log(data),
        error: error => console.log(error)
      })
  }
}

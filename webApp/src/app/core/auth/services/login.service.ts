import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(
    private httpClient: HttpClient
  ) { }

  loginCandidatos(email: string) {
    const baseUrl = environment.HOST_CAND + 'candidato?mail=' + email;
    return this.httpClient.get(baseUrl);
  }
  loginEmpresas(email: string) {
    const baseUrl = environment.HOST_EMP + 'empresa?mail=' + email;
    return this.httpClient.get(baseUrl);
  }
}

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class BusquedaService {

  constructor(private httpClient: HttpClient) { }

  searchCandidates(companyId: number, projectId: number, profileId: number): Observable<any>{
    let baseUrl: string = environment.HOST_BUSQ + 'empresa/' + companyId + '/proyecto/' + projectId + '/perfil/' + profileId + '/busqueda';
    return this.httpClient.post<any>(baseUrl, {});
  }

  provisionalKillSearch(companyId: number, projectId: number, profileId: number, searchId: number): Observable<any>{
    let baseUrl: string = environment.HOST_BUSQ + 'empresa/' + companyId + '/proyecto/' + projectId + '/perfil/' + profileId + '/busqueda/' + searchId + '/run';
    return this.httpClient.post<any>(baseUrl, {});
  }

  getSearchResults(companyId: number, projectId: number, profileId: number, searchId: number): Observable<any>{
    let baseUrl: string = environment.HOST_BUSQ + 'empresa/' + companyId + '/proyecto/' + projectId + '/perfil/' + profileId + '/busqueda/' + searchId;
    return this.httpClient.get<any>(baseUrl);
  }
}

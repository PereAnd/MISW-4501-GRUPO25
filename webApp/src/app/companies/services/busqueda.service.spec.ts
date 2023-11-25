import { TestBed } from '@angular/core/testing';

import { BusquedaService } from './busqueda.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { environment } from 'src/environments/environment.development';
import { faker } from '@faker-js/faker';

describe('BusquedaService', () => {
  let service: BusquedaService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [BusquedaService],
    });
    service = TestBed.inject(BusquedaService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'BusquedaService'", () => {
    expect(service).toBeTruthy();
  });
  it("Método 'searchCandidates', servicio 'BusquedaService'", () => {
    const empresaId: number = 1;
    const proyectoId: number = 1;
    const perfilId: number = 1;
    const baseUrl = environment.HOST_BUSQ + 'empresa/' + empresaId + '/proyecto/' + proyectoId + '/perfil/' + perfilId + '/busqueda';
    const mockResponse = [
      {
        "id": 1,
        "resultados": [],
        "perfilId": 1,
        "status": "INIT",
        "searchDate": "2023-11-25T14:06:52.804883"
      }
    ];

    service.searchCandidates(empresaId, proyectoId, perfilId).subscribe({
      next: (response) => {
        expect(response).toEqual(mockResponse);
      },
    });
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('POST');

    req.flush(mockResponse);
  });
  it("Método 'getSearchResults', servicio 'BusquedaService'", () => {
    const empresaId: number = 1;
    const proyectoId: number = 1;
    const perfilId: number = 1;
    const busquedaId: number = 1;
    const baseUrl = environment.HOST_BUSQ + 'empresa/' + empresaId + '/proyecto/' + proyectoId + '/perfil/' + perfilId + '/busqueda/' + busquedaId;
    const mockResponse = {
      "id": 1,
      "resultados": [
          {
            "id": 1,
            "candidatoId": 1,
            "busquedaId": 1
          },
          {
            "id": 2,
            "candidatoId": 2,
            "busquedaId": 1
          }
      ],
      "perfilId": 1,
      "status": "Finalizado",
      "searchDate": "2023-11-25T14:06:26.514916"
    }

    service.getSearchResults(empresaId, proyectoId, perfilId, busquedaId).subscribe({
      next: (response) => {
        expect(response).toEqual(mockResponse);
      },
    });
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  });
});

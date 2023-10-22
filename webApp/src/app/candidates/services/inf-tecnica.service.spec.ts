import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';

import { environment } from 'src/environments/environment.development';
import { faker } from '@faker-js/faker'
import { InfTecnicaService } from './inf-tecnica.service';
import { InfoTecnica } from '../models/info-tecnica';

describe('InfTecnicaService', () => {
  let service: InfTecnicaService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [InfTecnicaService]
    });
    service = TestBed.inject(InfTecnicaService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'InfTecnicaService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'listInfoTecnica', servicio 'InfTecnicaService'", () => {
    const candidatoId: number = 1;
    const baseUrl = environment.HOST + 'candidato/' + candidatoId + '/informacionTecnica';
    const mockResponse = [
      {
        "type": faker.lorem.word(),
        "description": faker.lorem.words(5)
      },
      {
        "type": faker.lorem.word(),
        "description": faker.lorem.words(5)
      }
    ]

    service.listInfoTecnica(candidatoId).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'addInfoTecnica', servicio 'InfTecnicaService'", () => {
    const candidatoId = 1;
    const baseUrl = environment.HOST + 'candidato/' + candidatoId + '/informacionTecnica';

    const newInfoTecnica: InfoTecnica = new InfoTecnica(
      faker.lorem.word(),
      faker.lorem.words(5)
    );
    const mockResponse = {
      "id": newInfoTecnica.id,
      "type": newInfoTecnica.type,
      "description": newInfoTecnica.description
    }
    service.addInfoTecnica(newInfoTecnica, candidatoId).subscribe({
      next: response => {
        response = <InfoTecnica>response
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('POST');

    req.flush(mockResponse);
  })

  it("Método 'findInfoTecnica', servicio 'InfTecnicaService'", () => {
    const candidatoId = 1;
    const indexInfoTec = 1;
    const baseUrl = environment.HOST + 'candidato/' + candidatoId + '/informacionTecnica/' + indexInfoTec;

    const mockResponse = {
      "id": 1,
      "type": faker.lorem.word(),
      "description": faker.lorem.words(5)
    }

    service.findInfoTecnica(candidatoId, indexInfoTec).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'editInfoTecnica', servicio 'InfTecnicaService'", () => {
    const candidatoId = 1;
    const indexInfoTec = 1;
    const baseUrl = environment.HOST + 'candidato/' + candidatoId + '/informacionTecnica/' + indexInfoTec;

    const newInfoTecnica: InfoTecnica = new InfoTecnica(
      faker.lorem.word(),
      faker.lorem.words(5)
    );
    const mockResponse = {
      "id": 1,
      "type": newInfoTecnica.type,
      "description": newInfoTecnica.description
    }
    service.editInfoTecnica(newInfoTecnica, indexInfoTec, candidatoId).subscribe({
      next: response => {
        response = <InfoTecnica>response
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('PATCH');

    req.flush(mockResponse);
  })

  afterEach(() => {
    httpMock.verify();
  })
});

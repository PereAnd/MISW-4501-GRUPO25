import { TestBed } from '@angular/core/testing';

import { InfLaboralService } from './inf-laboral.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { environment } from 'src/environments/environment.development';
import { faker } from '@faker-js/faker';
import { InfoLaboral } from '../models/info-laboral';

describe('InfLaboralService', () => {
  let service: InfLaboralService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [InfLaboralService]
    });
    service = TestBed.inject(InfLaboralService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'InfLaboralService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'listInfoLaboral', servicio 'InfLaboralService'", () => {
    const baseUrl = environment.HOST_CAND + 'candidato/1/informacionLaboral';
    const mockResponse = [
      {
        "id": 1,
        "position": faker.person.jobTitle(),
        "organization": faker.company.name(),
        "dateFrom": faker.date.past().toISOString(),
        "dateTo": faker.date.recent().toISOString(),
        "activities": faker.lorem.paragraph()
      },
      {
        "id": 2,
        "position": faker.person.jobTitle(),
        "organization": faker.company.name(),
        "dateFrom": faker.date.past().toISOString(),
        "dateTo": faker.date.recent().toISOString(),
        "activities": faker.lorem.paragraph()
      }
    ]

    service.listInfoLaboral(1).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'addInfoLaboral', servicio 'InfLaboralService'", () => {
    const baseUrl = environment.HOST_CAND + 'candidato/1/informacionLaboral';
    const candidatoId = 1;

    const newInfoLaboral: InfoLaboral = new InfoLaboral(
      faker.person.jobTitle(),
      faker.company.name(),
      faker.date.past().toISOString(),
      faker.date.recent().toISOString(),
      faker.lorem.paragraph()
    );
    const mockResponse = {
      "id": 1,
      "position": newInfoLaboral.position,
      "organization": newInfoLaboral.organization,
      "dateFrom": newInfoLaboral.dateFrom,
      "dateTo": newInfoLaboral.dateTo,
      "activities": newInfoLaboral.activities
    }
    service.addInfoLaboral(newInfoLaboral, candidatoId).subscribe({
      next: response => {
        response = <InfoLaboral>response
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('POST');

    req.flush(mockResponse);
  })

  it("Método 'findInfoLaboral', servicio 'InfLaboralService'", () => {
    const baseUrl = environment.HOST_CAND + 'candidato/1/informacionLaboral/1';
    const candidatoId = 1;
    const indexInfoLab = 1;

    const mockResponse = {
      "id": 1,
      "position": faker.person.jobTitle(),
      "organization": faker.company.name(),
      "dateFrom": faker.date.past().toISOString(),
      "dateTo": faker.date.recent().toISOString(),
      "activities": faker.lorem.paragraph()
    }

    service.findInfoLaboral(candidatoId, indexInfoLab).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'editInfoLaboral', servicio 'InfLaboralService'", () => {
    const baseUrl = environment.HOST_CAND + 'candidato/1/informacionLaboral/1';
    const candidatoId = 1;
    const indexInfoLab = 1;

    const newInfoLaboral: InfoLaboral = new InfoLaboral(
      faker.person.jobTitle(),
      faker.company.name(),
      faker.date.past().toISOString(),
      faker.date.recent().toISOString(),
      faker.lorem.paragraph()
    );
    const mockResponse = {
      "id": 1,
      "position": newInfoLaboral.position,
      "organization": newInfoLaboral.organization,
      "dateFrom": newInfoLaboral.dateFrom,
      "dateTo": newInfoLaboral.dateTo,
      "activities": newInfoLaboral.activities
    }
    service.editInfoLaboral(newInfoLaboral, indexInfoLab, candidatoId).subscribe({
      next: response => {
        response = <InfoLaboral>response
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

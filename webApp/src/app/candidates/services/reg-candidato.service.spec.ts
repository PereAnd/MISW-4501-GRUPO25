import { TestBed } from '@angular/core/testing';

import { RegCandidatoService } from './reg-candidato.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { Candidato } from '../models/candidato';
import { faker, ne } from '@faker-js/faker';
import { environment } from 'src/environments/environment.development';

describe('RegCandidatoService', () => {
  let service: RegCandidatoService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [RegCandidatoService]
    });
    service = TestBed.inject(RegCandidatoService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'RegCandidatoService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'registrarCandidato', servicio 'RegCandidatoService'", () => {
    const pass: string = faker.lorem.word(10);
    const newCandidato: Candidato = new Candidato(
      faker.person.firstName(),
      faker.person.lastName(),
      faker.internet.email(),
      pass,
      pass
    )

    const baseUrl = environment.HOST + 'candidato';

    const mockResponse = {
      "id": 1,
      "names": newCandidato.names,
      "lastNames": newCandidato.lastNames,
      "mail": newCandidato.mail
    }

    service.registrarCandidato(newCandidato).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('POST');

    req.flush(mockResponse);
  })

  it("Método 'getDatosCandidato', servicio 'RegCandidatoService'", () => {
    const candidatoId: number = 1;
    const baseUrl = environment.HOST + 'candidato/' + candidatoId;
    const mockResponse = {
      "id": 1,
      "names": faker.person.firstName(),
      "lastNames": faker.person.lastName(),
      "mail": faker.internet.email(),
      "docType": 'Cedula de Ciudadanía',
      "phone": faker.phone.number(),
      "address": faker.location.streetAddress(),
      "birthDate": faker.date.past(),
      "country": faker.location.country(),
      "city": faker.location.city(),
      "language": 'English',
      "informacionAcademica": [],
      "informacionTecnica": []
    }

    service.getDatosCandidato(candidatoId).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'updateDatosCandidato', servicio 'RegCandidatoService'", () => {
    const candidatoId: number = 1;
    const pass: string = faker.lorem.word(10);
    const baseUrl = environment.HOST + 'candidato/' + candidatoId;

    const newCandidato: Candidato = new Candidato(
      faker.person.firstName(),
      faker.person.lastName(),
      faker.internet.email(),
      pass,
      pass,
      'Cedula de Ciudadanía',
      faker.phone.number(),
      faker.location.streetAddress(),
      faker.date.past(),
      faker.location.country(),
      faker.location.city(),
      'English',
      candidatoId,
      [],
      []
    )
    const mockResponse = {
      "id": 1,
      "names": faker.person.firstName(),
      "lastNames": faker.person.lastName(),
      "mail": faker.internet.email(),
      "docType": 'Cedula de Ciudadanía',
      "phone": faker.phone.number(),
      "address": faker.location.streetAddress(),
      "birthDate": faker.date.past(),
      "country": faker.location.country(),
      "city": faker.location.city(),
      "language": 'English',
      "informacionAcademica": [],
      "informacionTecnica": []
    }

    service.updateDatosCandidato(newCandidato).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('PATCH');

    req.flush(mockResponse);
  })
});

import { TestBed } from '@angular/core/testing';

import { LoginService } from './login.service';
import {
  HttpClientTestingModule,
  HttpTestingController,
} from '@angular/common/http/testing';
import { faker } from '@faker-js/faker';
import { environment } from 'src/environments/environment.development';

describe('LoginService', () => {
  let service: LoginService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [LoginService],
    });
    service = TestBed.inject(LoginService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'LoginService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'loginCandidatos', servicio 'LoginService'", () => {
    const email = faker.internet.email();
    const baseUrl = environment.HOST_CAND + 'candidato?mail=' + email;

    const mockResponse = [
      {
        language: faker.lorem.word(10),
        informacionTecnica: [],
        names: faker.person.firstName(),
        id: 1,
        mail: email,
        docType: faker.lorem.word(10),
        informacionAcademica: [],
        birthDate: faker.date.past(),
        lastNames: faker.person.lastName(),
        country: faker.location.country(),
        docNumber: faker.number.int(),
        city: faker.location.city(),
        address: faker.location.streetAddress(),
        phone: faker.number.int(),
      },
    ];

    service.loginCandidatos(email).subscribe({
      next: (response) => {
        expect(response).toEqual(mockResponse);
      },
    });
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  });

  it("Método 'loginEmpresas', servicio 'LoginService'", () => {
    const email = faker.internet.email();
    const baseUrl = environment.HOST_EMP + 'empresa?mail=' + email;

    const mockResponse = [
      {
        description: faker.lorem.paragraph(5),
        organizationType: faker.lorem.word(),
        mail: email,
        docType: faker.lorem.word(),
        vertical: [],
        ubicacion: [],
        name: faker.company.name(),
        docNumber: faker.number.int(),
        id: 1,
      },
    ];

    service.loginEmpresas(email).subscribe({
      next: (response) => {
        expect(response).toEqual(mockResponse);
      },
    });
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  });

  afterEach(() => {
    httpMock.verify();
  });
});

import { TestBed } from '@angular/core/testing';

import { PerfilesService } from './perfiles.service';
import {
  HttpClientTestingModule,
  HttpTestingController,
} from '@angular/common/http/testing';
import { environment } from 'src/environments/environment.development';
import { faker } from '@faker-js/faker';
import { Perfil } from '../models/perfil';

describe('PerfilesService', () => {
  let service: PerfilesService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [PerfilesService],
    });
    service = TestBed.inject(PerfilesService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'PerfilesService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'listPerfiles', servicio 'PerfilesService'", () => {
    const empresaId: number = 1;
    const proyectoId: number = 1;
    const baseUrl =
      environment.HOST_PERF +
      'empresa/' +
      empresaId +
      '/proyecto/' +
      proyectoId +
      '/perfil';
    const mockResponse = [
      {
        name: faker.person.jobTitle(),
        role: faker.person.jobType(),
        location: faker.location.county(),
        years: Math.random() * 5,
      },
      {
        name: faker.person.jobTitle(),
        role: faker.person.jobType(),
        location: faker.location.county(),
        years: Math.random() * 5,
      },
    ];

    service.listPerfiles(empresaId, proyectoId).subscribe({
      next: (response) => {
        expect(response).toEqual(mockResponse);
      },
    });
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  });

  // Test the 'addPerfil' method of the 'PerfilesService' service.

  it("Método 'addPerfil', servicio 'PerfilesService'", () => {
    const proyectoId: number = 1;
    const empresaId: number = 1;
    const perfil: Perfil = {
      name: faker.person.jobTitle(),
      role: faker.person.jobType(),
      location: faker.location.county(),
      years: Math.random() * 5,
    };
    const baseUrl =
      environment.HOST_PERF +
      'empresa/' +
      empresaId +
      '/proyecto/' +
      proyectoId +
      '/perfil';
    const mockResponse = {
      name: faker.person.jobTitle(),
      role: faker.person.jobType(),
      location: faker.location.county(),
      years: Math.random() * 5,
    };

    service.addPerfil(proyectoId, empresaId, perfil).subscribe({
      next: (response) => {
        expect(response).toEqual(mockResponse);
      },
    });
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('POST');

    req.flush(mockResponse);
  });

  // Test the 'editPerfil' method of the 'PerfilesService' service.

  it("Método 'editPerfil', servicio 'PerfilesService'", () => {
    const proyectoId: number = 1;
    const empresaId: number = 1;
    const perfilId: number = 1;
    const perfil: Perfil = {
      name: faker.person.jobTitle(),
      role: faker.person.jobType(),
      location: faker.location.county(),
      years: Math.random() * 5,
    };
    const baseUrl =
      environment.HOST_PERF +
      'empresa/' +
      empresaId +
      '/proyecto/' +
      proyectoId +
      '/perfil/' +
      perfilId;
    const mockResponse = {
      name: faker.person.jobTitle(),
      role: faker.person.jobType(),
      location: faker.location.county(),
      years: Math.random() * 5,
    };

    service.editPerfil(proyectoId, empresaId, perfilId, perfil).subscribe({
      next: (response) => {
        expect(response).toEqual(mockResponse);
      },
    });
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('PATCH');

    req.flush(mockResponse);
  });
});

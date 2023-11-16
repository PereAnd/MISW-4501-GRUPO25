import { TestBed } from '@angular/core/testing';

import { UbicacionesService } from './ubicaciones.service';
import { HttpTestingController, HttpClientTestingModule } from '@angular/common/http/testing';
import { faker } from '@faker-js/faker';
import { environment } from 'src/environments/environment.development';
import { Ubicacion } from '../models/empresas';

describe('UbicacionesService', () => {
  let service: UbicacionesService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [UbicacionesService]
    });
    service = TestBed.inject(UbicacionesService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'UbicacionesService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'listUbicaciones', servicio 'UbicacionesService'", () => {
    const empresaId: number = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/ubicacion';
    const mockResponse = [
      {
        "country": faker.location.country(),
        "city": faker.location.city(),
        "description": faker.lorem.words(5)
      },
      {
        "country": faker.location.country(),
        "city": faker.location.city(),
        "description": faker.lorem.words(5)
      }
    ]

    service.listUbicaciones(empresaId).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'addUbicacion', servicio 'UbicacionesService'", () => {
    const empresaId = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/ubicacion';

    const newUbicacion: Ubicacion = new Ubicacion(
      faker.location.country(),
      faker.location.city(),
      faker.lorem.words(5)
    );
    const mockResponse = {
      "country": newUbicacion.country,
      "city": newUbicacion.city,
      "description": newUbicacion.description
    }
    service.addUbicacion(newUbicacion, empresaId).subscribe({
      next: response => {
        response = <Ubicacion>response
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('POST');

    req.flush(mockResponse);
  })

  it("Método 'findUbicacion', servicio 'UbicacionesService'", () => {
    const empresaId = 1;
    const indexUbicacion = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/ubicacion/' + indexUbicacion;

    const mockResponse = {
      "id": indexUbicacion,
      "country": faker.location.country(),
      "city": faker.location.city(),
      "description": faker.lorem.words(5)
    }

    service.findUbicacion(empresaId, indexUbicacion).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'editUbicacion', servicio 'UbicacionesService'", () => {
    const empresaId = 1;
    const indexUbicacion = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/ubicacion/' + indexUbicacion;

    const newUbicacion: Ubicacion = new Ubicacion(
      faker.location.country(),
      faker.location.city(),
      faker.lorem.words(5)
    );
    const mockResponse = {
      "id": 1,
      "country": newUbicacion.country,
      "city": newUbicacion.city,
      "description": newUbicacion.description
    }
    service.editUbicacion(newUbicacion, indexUbicacion, empresaId).subscribe({
      next: response => {
        response = <Ubicacion>response
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

import { TestBed } from '@angular/core/testing';

import { VerticalesService } from './verticales.service';
import { HttpTestingController, HttpClientTestingModule } from '@angular/common/http/testing';
import { faker } from '@faker-js/faker';
import { environment } from 'src/environments/environment.development';
import { Vertical } from '../models/vertical';

describe('VerticalesService', () => {
  let service: VerticalesService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [VerticalesService]
    });
    service = TestBed.inject(VerticalesService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'VerticalesService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'listVerticales', servicio 'VerticalesService'", () => {
    const empresaId: number = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/vertical';
    const mockResponse = [
      {
        "vertical": faker.lorem.word(),
        "description": faker.lorem.paragraph(5),
        "id": 1,
      },
      {
        "vertical": faker.lorem.word(),
        "description": faker.lorem.paragraph(5),
        "id": 2,
      }
    ]

    service.listVerticales(empresaId).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'addVertical', servicio 'VerticalesService'", () => {
    const empresaId = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/vertical';

    const newVertical: Vertical = new Vertical(
      faker.lorem.word(),
      faker.lorem.paragraph()
    );
    const mockResponse = {
      "id": newVertical.id,
      "vertical": newVertical.vertical,
      "description": newVertical.description
    }
    service.addVertical(newVertical, empresaId).subscribe({
      next: response => {
        response = <Vertical>response
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('POST');

    req.flush(mockResponse);
  })

  it("Método 'findVertical', servicio 'VerticalesService'", () => {
    const empresaId = 1;
    const indexVertical = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/vertical/' + indexVertical;

    const mockResponse = {
      "id": 1,
      "vertical": faker.lorem.word(),
      "description": faker.lorem.paragraph(5)
    }

    service.findVertical(empresaId, indexVertical).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'editVertical', servicio 'VerticalesService'", () => {
    const empresaId = 1;
    const indexVertical = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/vertical/' + indexVertical;

    const newVertical: Vertical = new Vertical(
      faker.lorem.word(),
      faker.lorem.paragraph(5)
    );
    const mockResponse = {
      "id": 1,
      "vertical": newVertical.vertical,
      "description": newVertical.description
    }
    service.editVertical(newVertical, indexVertical, empresaId).subscribe({
      next: response => {
        response = <Vertical>response
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

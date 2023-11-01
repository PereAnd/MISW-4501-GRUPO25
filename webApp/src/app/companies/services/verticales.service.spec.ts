import { TestBed } from '@angular/core/testing';

import { VerticalesService } from './verticales.service';
import { HttpTestingController, HttpClientTestingModule } from '@angular/common/http/testing';
import { faker } from '@faker-js/faker';
import { environment } from 'src/environments/environment.development';

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
});

import { TestBed } from '@angular/core/testing';

import { ProyectosService } from './proyectos.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { environment } from 'src/environments/environment.development';
import { faker } from '@faker-js/faker';

describe('ProyectosService', () => {
  let service: ProyectosService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [ProyectosService]
    });
    service = TestBed.inject(ProyectosService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'ProyectosService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'listProyectos', servicio 'ProyectosService'", () => {
    const empresaId: number = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/proyecto';
    const mockResponse = [
      {
        "proyecto": faker.lorem.words(3),
        "description": faker.lorem.words(5)
      },
      {
        "proyecto": faker.lorem.words(3),
        "description": faker.lorem.words(5)
      }
    ]

    service.listProyectos(empresaId).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })
});

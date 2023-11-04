import { TestBed } from '@angular/core/testing';

import { ProyectosService } from './proyectos.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { environment } from 'src/environments/environment.development';
import { faker } from '@faker-js/faker';
import { Proyecto } from '../models/proyecto';

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

  it("Método 'addProyecto', servicio 'ProyectosService'", () => {
    const empresaId = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/proyecto';

    const newProyecto: Proyecto = new Proyecto(
      faker.lorem.words(3),
      faker.lorem.words(5)
    );
    const mockResponse = {
      "id": newProyecto.id,
      "proyecto": newProyecto.proyecto,
      "description": newProyecto.description
    }
    service.addProyecto(newProyecto, empresaId).subscribe({
      next: response => {
        response = <Proyecto>response
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('POST');

    req.flush(mockResponse);
  })

  it("Método 'findProyecto', servicio 'ProyectosService'", () => {
    const empresaId = 1;
    const indexProyecto = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/proyecto/' + indexProyecto;

    const mockResponse = {
      "id": 1,
      "proyecto": faker.lorem.words(3),
      "description": faker.lorem.words(5)
    }

    service.findProyecto(empresaId, indexProyecto).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'editProyecto', servicio 'ProyectosService'", () => {
    const empresaId = 1;
    const indexProyecto = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId + '/proyecto/' + indexProyecto;

    const newProyecto: Proyecto = new Proyecto(
      faker.lorem.words(3),
      faker.lorem.words(5)
    );
    const mockResponse = {
      "id": 1,
      "proyecto": newProyecto.proyecto,
      "description": newProyecto.description
    }
    service.editProyecto(newProyecto, indexProyecto, empresaId).subscribe({
      next: response => {
        response = <Proyecto>response
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

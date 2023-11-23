import { TestBed } from '@angular/core/testing';

import { RegEmpresaService } from './reg-empresa.service'
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { faker } from '@faker-js/faker';
import { Empresa, Ubicacion, Vertical } from '../models/empresas';
import { environment } from 'src/environments/environment.development';

describe('Servicio RegEmpresaService', () => {
  let service: RegEmpresaService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [RegEmpresaService]
    });
    service = TestBed.inject(RegEmpresaService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'RegEmpresaService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'registrarEmpresa', servicio 'RegEmpresaService'", () => {
    const pass: string = faker.lorem.word(10);
    const newEmpresa: Empresa = new Empresa(
      faker.company.name(),
      faker.internet.email(),
      pass,
      pass
    )
    const baseUrl = environment.HOST_EMP + 'empresa';

    const mockResponse = {
      "id": 1,
      "name": newEmpresa.name,
      "mail": newEmpresa.mail
    }
    service.registrarEmpresa(newEmpresa).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('POST');

    req.flush(mockResponse);
  })

  it("Método 'getDatosEmpresa', servicio 'RegEmpresaService'", () => {
    const empresaId: number = 1;
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId;
    const mockResponse = {
      "id": 1,
      "name": faker.company.name(),
      "organizationType": faker.company.buzzPhrase(),
      "mail": faker.internet.email(),
      "docType": 'NIT',
      "docNumber": faker.phone.number(),
      "description": faker.lorem.paragraph(5)
    }

    service.getDatosEmpresa(empresaId).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'updateDatosEmpresa', servicio 'RegEmpresaService'", () => {
    const empresaId: number = 1;
    const pass: string = faker.lorem.word(10);
    const baseUrl = environment.HOST_EMP + 'empresa/' + empresaId;

    const newEmpresa: Empresa = new Empresa(
      faker.company.name(),
      faker.internet.email(),
      pass,
      pass,
      faker.company.buzzPhrase(),
      'NIT',
      faker.phone.number(),
      faker.lorem.paragraph(5),
      empresaId
    )
    const mockResponse = {
      "id": empresaId,
      "name": newEmpresa.name,
      "organizationType": newEmpresa.organizationType,
      "mail": newEmpresa.mail,
      "docType": newEmpresa.docType,
      "docNumber": newEmpresa.docNumber,
      "description": newEmpresa.description
    }

    service.updateDatosEmpresa(newEmpresa).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('PATCH');
    req.flush(mockResponse);
  })
  it("Creación de la instancia de 'EmpresasService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'listVerticales', servicio 'EmpresasService'", () => {
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

  it("Método 'addVertical', servicio 'EmpresasService'", () => {
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

  it("Método 'findVertical', servicio 'EmpresasService'", () => {
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

  it("Método 'editVertical', servicio 'EmpresasService'", () => {
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

  it("Creación de la instancia de 'EmpresasService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'listUbicaciones', servicio 'EmpresasService'", () => {
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

  it("Método 'addUbicacion', servicio 'EmpresasService'", () => {
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

  it("Método 'findUbicacion', servicio 'EmpresasService'", () => {
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

  it("Método 'editUbicacion', servicio 'EmpresasService'", () => {
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

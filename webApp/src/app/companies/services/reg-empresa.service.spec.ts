import { TestBed } from '@angular/core/testing';

import { RegEmpresaService } from './reg-empresa.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { faker } from '@faker-js/faker';
import { Empresa } from '../models/empresa';
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
});

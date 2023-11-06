import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { InfAcademicaService } from './inf-academica.service';
import { environment } from 'src/environments/environment.development';
import { InfoAcademica } from '../models/info-academica'
import { faker } from '@faker-js/faker';


describe('InfAcademicaService', () => {

  let service: InfAcademicaService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [InfAcademicaService]
    });
    service = TestBed.inject(InfAcademicaService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("Creación de la instancia de 'InfAcademicaService'", () => {
    expect(service).toBeTruthy();
  });

  it("Método 'listInfoAcademica', servicio 'InfAcademicaService'", () => {
    const baseUrl = environment.HOST_CAND + 'candidato/1/informacionAcademica';
    const mockResponse = [
      {
        "id": 1,
        "title": faker.person.jobTitle(),
        "institution": faker.company.name(),
        "beginDate": faker.date.past().toISOString(),
        "endDate": faker.date.recent().toISOString(),
        "studyType": faker.person.jobType()
      },
      {
        "id": 2,
        "title": faker.person.jobTitle(),
        "institution": faker.company.name(),
        "beginDate": faker.date.past().toISOString(),
        "endDate": faker.date.recent().toISOString(),
        "studyType": faker.person.jobType()
      }
    ]

    service.listInfoAcademica(1).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })
    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'addInfoAcademica', servicio 'InfAcademicaService'", () => {
    const baseUrl = environment.HOST_CAND + 'candidato/1/informacionAcademica';
    const candidatoId = 1;

    const newInfoAcademica: InfoAcademica = new InfoAcademica(
      faker.person.jobTitle(),
      faker.company.name(),
      faker.date.past().toISOString(),
      faker.date.recent().toISOString(),
      faker.person.jobType()
    );
    const mockResponse = {
      "id": 1,
      "title": newInfoAcademica.title,
      "institution": newInfoAcademica.institution,
      "beginDate": newInfoAcademica.beginDate,
      "endDate": newInfoAcademica.endDate,
      "studyType": newInfoAcademica.studyType
    }
    service.addInfoAcademica(newInfoAcademica, candidatoId).subscribe({
      next: response => {
        response = <InfoAcademica>response
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('POST');

    req.flush(mockResponse);
  })

  it("Método 'findInfoAcademica', servicio 'InfAcademicaService'", () => {
    const baseUrl = environment.HOST_CAND + 'candidato/1/informacionAcademica/1';
    const candidatoId = 1;
    const indexInfoAcad = 1;

    const mockResponse = {
      "id": 1,
      "title": faker.person.jobTitle(),
      "institution": faker.company.name(),
      "beginDate": faker.date.past().toISOString(),
      "endDate": faker.date.recent().toISOString(),
      "studyType": faker.person.jobType()
    }

    service.findInfoAcademica(candidatoId, indexInfoAcad).subscribe({
      next: response => {
        expect(response).toEqual(mockResponse)
      }
    })

    const req = httpMock.expectOne(baseUrl);
    expect(req.request.method).toBe('GET');

    req.flush(mockResponse);
  })

  it("Método 'editInfoAcademica', servicio 'InfAcademicaService'", () => {
    const baseUrl = environment.HOST_CAND + 'candidato/1/informacionAcademica/1';
    const candidatoId = 1;
    const indexInfoAcad = 1;

    const newInfoAcademica: InfoAcademica = new InfoAcademica(
      faker.person.jobTitle(),
      faker.company.name(),
      faker.date.past().toISOString(),
      faker.date.recent().toISOString(),
      faker.person.jobType()
    );
    const mockResponse = {
      "id": 1,
      "title": newInfoAcademica.title,
      "institution": newInfoAcademica.institution,
      "beginDate": newInfoAcademica.beginDate,
      "endDate": newInfoAcademica.endDate,
      "studyType": newInfoAcademica.studyType
    }
    service.editInfoAcademica(newInfoAcademica, indexInfoAcad, candidatoId).subscribe({
      next: response => {
        response = <InfoAcademica>response
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

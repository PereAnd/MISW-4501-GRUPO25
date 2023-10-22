import { faker } from '@faker-js/faker';
import { InfoAcademica } from './info-academica';
import { TestBed } from '@angular/core/testing';

describe('InfoAcademica', () => {
  let infoAcademica: InfoAcademica;
  let studyType: string[] = ['Pregrado', 'Posgrado']

  const dataFake = {
    title: faker.person.jobTitle(),
    institution: faker.company.name(),
    beginDate: faker.date.past(),
    endDate: faker.date.past(),
    studyType: studyType[Math.floor(Math.random() * studyType.length)],
    candidateId: 1
  }

  beforeEach(() => {
    TestBed.configureTestingModule({});
    infoAcademica = new InfoAcademica(
      dataFake.title,
      dataFake.institution,
      dataFake.beginDate.toISOString(),
      dataFake.endDate.toISOString(),
      dataFake.studyType,
      dataFake.candidateId
    );
  })
  it("Crear instancia de 'InfoAcademica'", () => {
    expect(infoAcademica).toBeTruthy();
  })
});

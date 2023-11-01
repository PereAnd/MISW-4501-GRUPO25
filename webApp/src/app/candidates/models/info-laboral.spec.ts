import { faker } from '@faker-js/faker';
import { InfoLaboral } from './info-laboral';
import { TestBed } from '@angular/core/testing';

describe('InfoLaboral', () => {
  let infoLaboral: InfoLaboral;

  const dataFake = {
    position: faker.person.jobTitle(),
    organization: faker.company.name(),
    dateFrom: faker.date.past(),
    dateTo: faker.date.past(),
    activities: faker.lorem.paragraph(),
    candidateId: 1
  }

  beforeEach(() => {
    TestBed.configureTestingModule({});
    infoLaboral = new InfoLaboral(
      dataFake.position,
      dataFake.organization,
      dataFake.dateFrom.toISOString(),
      dataFake.dateTo.toISOString(),
      dataFake.activities,
      dataFake.candidateId
    );
  })
  it("Crear instancia de 'InfoLaboral'", () => {
    expect(infoLaboral).toBeTruthy();
  })
});

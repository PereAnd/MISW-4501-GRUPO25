import { TestBed } from '@angular/core/testing';
import { Candidato } from './candidato';
import { faker } from '@faker-js/faker'

describe('Candidato', () => {
  let candidato: Candidato;

  const password = faker.phone.imei();

  const dataFake = {
    names: faker.person.firstName(),
    lastNames: faker.person.lastName(),
    mail: faker.internet.email(),
    password: password,
    confirmPassword: password
  }

  beforeEach(() => {
    TestBed.configureTestingModule({});
    candidato = new Candidato(
      dataFake.names,
      dataFake.lastNames,
      dataFake.mail,
      dataFake.password,
      dataFake.confirmPassword
    );
  })
  it("Crear instancia de 'Candidato'", () => {
    expect(candidato).toBeTruthy();
  })
});

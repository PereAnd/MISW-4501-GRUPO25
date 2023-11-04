import { faker } from '@faker-js/faker';
import { Empresa } from './empresa';
import { TestBed } from '@angular/core/testing';

describe('Class Empresa', () => {
  let empresa: Empresa;

  const password = faker.phone.imei();

  const dataFake = {
    name: faker.company.name(),
    email: faker.internet.email(),
    password: password,
    confirmPassword: password
  }

  beforeEach(() => {
    TestBed.configureTestingModule({});
    empresa = new Empresa(
      dataFake.name,
      dataFake.email,
      dataFake.password,
      dataFake.confirmPassword
    );
  })
  it("Crear instancia de la clase 'Empresa'", () => {
    expect(empresa).toBeTruthy();
  })
});

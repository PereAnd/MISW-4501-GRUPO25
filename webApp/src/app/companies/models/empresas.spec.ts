import { faker } from '@faker-js/faker';
import { Empresa, Ubicacion, Vertical } from './empresas';
import { TestBed } from '@angular/core/testing';

describe('Class Empresa', () => {
  let empresa: Empresa;
  let ubicacion: Ubicacion;
  let vertical: Vertical;

  const password = faker.phone.imei();
  const fakeEmpresa = {
    name: faker.company.name(),
    email: faker.internet.email(),
    password: password,
    confirmPassword: password
  }

  const fakeUbicacion = {
    country: faker.location.country(),
    city: faker.location.city(),
    description: faker.lorem.words(5)
  }

  const fakeVertical = {
    vertical: faker.company.buzzPhrase(),
    description: faker.lorem.paragraph(5)
  }

  beforeEach(() => {
    TestBed.configureTestingModule({});

  })
  it("Crear instancia de la clase 'Empresa'", () => {
    empresa = new Empresa(
      fakeEmpresa.name,
      fakeEmpresa.email,
      fakeEmpresa.password,
      fakeEmpresa.confirmPassword
    );
    expect(empresa).toBeTruthy();
  })
  it("Crear instancia de la clase 'Ubicacion'", () => {
    ubicacion = {
      country: faker.location.country(),
      city: faker.location.city(),
      description: faker.lorem.words(5)
    }
    expect(ubicacion).toBeTruthy();
  })
  it("Crear instancia de la clase 'Vertical'", () => {
    vertical = {
      vertical: faker.company.buzzPhrase(),
      description: faker.lorem.paragraph(5)
    }
    expect(vertical).toBeTruthy();
  })
});

import { faker } from '@faker-js/faker';
import { Perfil } from './perfil';
import { TestBed } from '@angular/core/testing';

describe('Perfil', () => {
  let perfil: Perfil;

  const dataFake = {
    name: faker.person.jobTitle(),
    role: faker.person.jobArea(),
    location: faker.location.country(),
    years: Math.random() * 5
  }

  beforeEach(() => {
    TestBed.configureTestingModule({});
    perfil = new Perfil(
      dataFake.name,
      dataFake.role,
      dataFake.location,
      dataFake.years
    );
  })
  it("Crear instancia de la clase 'Perfil'", () => {
    expect(perfil).toBeTruthy();
  })
});

import { faker } from '@faker-js/faker';
import { Ubicacion } from './ubicacion';
import { TestBed } from '@angular/core/testing';

describe('Ubicacion', () => {
  let ubicacion: Ubicacion;

  const dataFake = {
    country: faker.location.country(),
    city: faker.location.city(),
    description: faker.lorem.words(5)
  }

  beforeEach(() => {
    TestBed.configureTestingModule({});
    ubicacion = new Ubicacion(
      dataFake.country,
      dataFake.city,
      dataFake.description
    );
  })
  it("Crear instancia de la clase 'Ubicacion'", () => {
    expect(ubicacion).toBeTruthy();
  })
});

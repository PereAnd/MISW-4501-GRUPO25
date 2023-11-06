import { faker } from '@faker-js/faker';
import { Proyecto } from './proyecto';
import { TestBed } from '@angular/core/testing';

describe('Proyecto', () => {
  let proyecto: Proyecto;

  const dataFake = {
    proyecto: faker.lorem.words(3),
    description: faker.lorem.words(5)
  }

  beforeEach(() => {
    TestBed.configureTestingModule({});
    proyecto = new Proyecto(
      dataFake.proyecto,
      dataFake.description,
      1
    );
  })
  it("Crear instancia de la clase 'Proyecto'", () => {
    expect(proyecto).toBeTruthy();
  })
});

import { faker } from '@faker-js/faker';
import { Perfil, Proyecto } from './proyectos';
import { TestBed } from '@angular/core/testing';

describe('Proyecto', () => {
  let proyecto: Proyecto;
  let perfil: Perfil;

  const fakeProyecto = {
    proyecto: faker.lorem.words(3),
    description: faker.lorem.words(5)
  }
  const fakePerfil = {
    name: faker.person.jobTitle(),
    role: faker.person.jobArea(),
    location: faker.location.country(),
    years: Math.random() * 5
  }

  beforeEach(() => {
    TestBed.configureTestingModule({});
    proyecto = new Proyecto(
      fakeProyecto.proyecto,
      fakeProyecto.description,
      1
    );
    perfil = new Perfil(
      fakePerfil.name,
      fakePerfil.role,
      fakePerfil.location,
      fakePerfil.years
    );
  })
  it("Crear instancia de la clase 'Proyecto'", () => {
    expect(proyecto).toBeTruthy();
  })
  it("Crear instancia de la clase 'Perfil'", () => {
    expect(perfil).toBeTruthy();
  })
});

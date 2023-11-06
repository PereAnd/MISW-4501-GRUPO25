import { faker } from '@faker-js/faker';
import { Vertical } from './vertical';
import { TestBed } from '@angular/core/testing';

describe('Class Vertical', () => {
  let vertical: Vertical;

  const dataFake = {
    vertical: faker.company.buzzPhrase(),
    description: faker.lorem.paragraph(5)
  }

  beforeEach(() => {
    TestBed.configureTestingModule({});
    vertical = new Vertical(
      dataFake.vertical,
      dataFake.description
    );
  })
  it("Crear instancia de la clase 'Vertical'", () => {
    expect(vertical).toBeTruthy();
  })
});

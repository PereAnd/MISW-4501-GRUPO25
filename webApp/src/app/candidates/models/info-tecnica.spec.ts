import { faker } from '@faker-js/faker';
import { InfoTecnica } from './info-tecnica';


describe('InfoTecnica', () => {
  let infoTecnica: InfoTecnica;
  const typeInfoTec: string[] = ['Conocimiento', 'Habilidad']

  const dataFake = {
    type: typeInfoTec[Math.floor(Math.random() * typeInfoTec.length)],
    description: faker.lorem.words(5),
  }

  beforeEach(() => {
    infoTecnica = new InfoTecnica(
      dataFake.type,
      dataFake.description,
      1
    );
  })
  it("Crear instancia de 'InfoTecnica'", () => {
    expect(infoTecnica).toBeTruthy();
  })
});

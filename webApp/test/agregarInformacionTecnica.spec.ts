import { test, expect } from '@playwright/test';
import { faker } from '@faker-js/faker';

test('test', async ({ page }) => {
  await page.goto('http://bucket-abcjobs-angular.s3-website-us-east-1.amazonaws.com/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('jorge@gmail.com');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Rol').locator('span').click();
  await page.getByRole('option', { name: 'Candidato' }).click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Información Técnica' }).click();
  await page.getByRole('link', { name: 'Agregar nueva' }).click();
  await page.getByLabel('Tipo').click();
  await page.getByRole('option', { name: 'Idioma' }).click();
  await page.getByLabel('Descripción').click();
  await page.getByLabel('Descripción').fill('Ingles');
  await page.getByRole('button', { name: 'Guardar' }).click();
});

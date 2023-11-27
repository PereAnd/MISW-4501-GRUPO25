import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://bucket-abcjobs-angular.s3-website-us-east-1.amazonaws.com/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('jorge@gmail.com');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Rol').locator('svg').click();
  await page.getByRole('option', { name: 'Candidato' }).click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByRole('button', { name: 'Editar' }).click();
  await page.getByLabel('Teléfono').click();
  await page.getByLabel('Teléfono').fill('300393530');
  await page.getByLabel('Número de documento').click();
  await page.getByLabel('Número de documento').fill('110279579');
  await page.getByRole('button', { name: 'guardar' }).click();
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://bucket-abcjobs-angular.s3-website-us-east-1.amazonaws.com/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('jorge@gmail.com');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Rol').locator('span').click();
  await page.getByText('Candidato').click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Información Laboral' }).click();
  await page.getByRole('row', { name: '1 Ecopetrol Jefe Direccion estratégica, Liderazgo. 05 Jan 2016 08 Jul 2021' }).getByRole('link').click();
  await page.getByLabel('Empresa').click();
  await page.getByLabel('Empresa').press('CapsLock');
  await page.getByRole('button', { name: 'Guardar' }).click();
});

import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://bucket-abcjobs-angular.s3-website-us-east-1.amazonaws.com/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.locator('.mat-mdc-form-field-infix').first().click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('tecweb@gmail.com');
  await page.getByText('Contraseña', { exact: true }).click();
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Rol').locator('span').click();
  await page.getByRole('option', { name: 'Empresa' }).click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Verticales' }).click();
  await page.getByRole('link', { name: 'Agregar nueva' }).click();
  await page.locator('svg').click();
  await page.getByRole('option', { name: 'Desarrollo de Software' }).click();
  await page.getByLabel('Descripción').click();
  await page.getByLabel('Descripción').press('CapsLock');
  await page.getByLabel('Descripción').fill('Desarrollo web');
  await page.getByRole('button', { name: 'Guardar' }).click();
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

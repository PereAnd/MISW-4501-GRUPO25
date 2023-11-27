import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://bucket-abcjobs-angular.s3-website-us-east-1.amazonaws.com/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('tecweb@gmail.com');
  await page.getByLabel('Contraseña', { exact: true }).click();
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Rol').locator('svg').click();
  await page.getByRole('option', { name: 'Empresa' }).click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Ubicaciones' }).click();
  await page.getByRole('row', { name: '3' }).getByRole('link').click();
  await page.getByLabel('Descripción').click();
  await page.getByLabel('Descripción').fill('');
  await page.getByLabel('Descripción').press('CapsLock');
  await page.getByLabel('Descripción').fill('Sucursal');
  await page.getByRole('button', { name: 'Guardar' }).click();
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

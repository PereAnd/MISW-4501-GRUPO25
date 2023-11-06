import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.locator('#mat-mdc-form-field-label-0 span').click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('tecnoweb@gmail.com');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Rol').locator('svg').click();
  await page.getByRole('option', { name: 'Empresa' }).click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Ubicaciones' }).click();
  await page.getByRole('link', { name: 'Agregar nueva' }).click();
  await page.getByLabel('País').locator('svg').click();
  await page.getByRole('option', { name: 'Colombia' }).click();
  await page.getByLabel('Ciudad').locator('svg').click();
  await page.getByRole('option', { name: 'Medellín' }).click();
  await page.getByLabel('Descripción').click();
  await page.getByLabel('Descripción').press('CapsLock');
  await page.getByLabel('Descripción').fill('Principal');
  await page.getByRole('button', { name: 'Guardar' }).click();
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

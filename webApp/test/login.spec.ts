import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('j.cardonaouniandes.edu.co');
  await page.locator('#mat-mdc-form-field-label-2 span').click();
  await page.getByLabel('Contraseña', { exact: true }).fill('123456');
  await page.getByRole('link', { name: 'Ingresar' }).click();
});

import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('j.cardonaounandes.edu.co');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('123456');
  await page.getByRole('link', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Información Personal' }).click();
  await page.getByRole('button', { name: 'Editar' }).click();
  await page.getByLabel('Apellido').click();
  await page.getByLabel('Apellido').dblclick();
  await page.getByLabel('Apellido').dblclick();
  await page.getByLabel('Apellido').fill('');
  await page.getByLabel('Apellido').press('CapsLock');
  await page.getByLabel('Apellido').fill('Ortiz');
  await page.getByText('Teléfono').click();
  await page.getByLabel('Teléfono').fill('3003935273');
  await page.getByRole('button', { name: 'Guardar' }).click();
});

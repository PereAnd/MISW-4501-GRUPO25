import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByRole('link', { name: 'Crear cuenta' }).click();
  await page.getByLabel('Nombres').click();
  await page.getByLabel('Nombres').press('CapsLock');
  await page.getByLabel('Nombres').fill('Jorge');
  await page.getByLabel('Nombres').press('Tab');
  await page.getByLabel('Apellidos').press('CapsLock');
  await page.getByLabel('Apellidos').fill('Cardona');
  await page.getByLabel('Apellidos').press('Tab');
  await page.getByLabel('Correo').fill('j.cardonaouniandes.edu.co');
  await page.getByText('Contraseña', { exact: true }).click();
  await page.getByLabel('Contraseña', { exact: true }).fill('123456');
  await page.getByLabel('Contraseña', { exact: true }).press('Tab');
  await page.getByLabel('Confirmar contraseña').fill('123456');
  await page.getByRole('button', { name: 'Crear cuenta' }).click();
});

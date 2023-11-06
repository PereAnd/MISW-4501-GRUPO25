import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByRole('button', { name: 'Crear cuenta' }).click();
  await page.getByRole('menuitem', { name: 'Candidato' }).click();
  await page.getByText('Nombres').click();
  await page.getByLabel('Nombres').press('CapsLock');
  await page.getByLabel('Nombres').fill('Andres');
  await page.getByText('Apellidos').click();
  await page.getByLabel('Apellidos').press('CapsLock');
  await page.getByLabel('Apellidos').fill('Ortiz');
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('aortiz2@uniandes.edu.co');
  await page.getByText('Contraseña', { exact: true }).click();
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Contraseña', { exact: true }).press('Tab');
  await page.getByLabel('Confirmar contraseña').fill('qwerty');
  await page.getByRole('button', { name: 'Crear cuenta' }).click();
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('jcardonao@uniandes.edu.co');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Rol').locator('svg').click();
  await page.getByRole('option', { name: 'Candidato' }).click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByRole('button', { name: 'Editar' }).click();
  await page.getByLabel('Teléfono').click();
  await page.getByLabel('Teléfono').fill('3003935305');
  await page.getByLabel('Número de documento').click();
  await page.getByLabel('Número de documento').fill('1102795798');
  await page.getByRole('button', { name: 'Guardar' }).click();
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

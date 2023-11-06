import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('jcardonao@uniandes.edu.co');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Rol').locator('span').click();
  await page.getByText('Candidato').click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Información Laboral' }).click();
  await page.getByRole('row', { name: '10' }).getByRole('link').click();
  await page.getByLabel('Empresa').click();
  await page.getByLabel('Empresa').fill('');
  await page.getByLabel('Empresa').press('CapsLock');
  await page.getByLabel('Empresa').fill('Telmex');
  await page.getByRole('button', { name: 'Guardar' }).click();
});

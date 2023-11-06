import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('jcardonao@uniandes.edu.co');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('qwertt');
  await page.getByLabel('Rol').locator('span').click();
  await page.getByText('Candidato').click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Información Técnica' }).click();
  await page.getByRole('link', { name: 'Información Académica' }).click();
  await page.getByRole('row', { name: '18' }).getByRole('link').click();
  await page.getByLabel('Institución').click();
  await page.getByLabel('Institución').fill('');
  await page.getByLabel('Institución').click();
  await page.getByLabel('Institución').press('CapsLock');
  await page.getByLabel('Institución').fill('Uniandes');
  await page.getByRole('button', { name: 'Guardar' }).click();
});

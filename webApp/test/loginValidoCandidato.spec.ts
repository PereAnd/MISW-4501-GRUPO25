import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/login');
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('jcardonao@uniandes.edu.co');
  await page.getByText('Contraseña', { exact: true }).click();
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Rol').locator('span').click();
  await page.getByText('Candidato').click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

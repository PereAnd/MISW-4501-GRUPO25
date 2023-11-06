import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/login');
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByText('Correo').click();
  await page.getByLabel('Correo').fill('tecnoweb@gmail.com');
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByText('Contraseña', { exact: true }).click();
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByLabel('Rol').locator('path').click();
  await page.getByRole('option', { name: 'Empresa' }).click();
  page.once('dialog', dialog => {
    console.log(`Dialog message: ${dialog.message()}`);
    dialog.dismiss().catch(() => {});
  });
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByLabel('Rol').locator('svg').click();
  // await page.getByRole('option', { name: 'Candidato' }).click();
  page.once('dialog', dialog => {
    console.log(`Dialog message: ${dialog.message()}`);
    dialog.dismiss().catch(() => {});
  });
});

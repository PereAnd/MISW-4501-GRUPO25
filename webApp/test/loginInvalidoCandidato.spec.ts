import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/login');
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('jcardona@uniandes.edu.co');
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByText('Contraseña', { exact: true }).click();
  await page.getByLabel('Contraseña', { exact: true }).fill('123456');
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.locator('div').filter({ hasText: /^Rol$/ }).nth(2).click();
  await page.getByRole('option', { name: 'Candidato' }).click();
  page.once('dialog', dialog => {
    console.log(`Dialog message: ${dialog.message()}`);
    dialog.dismiss().catch(() => {});
  });
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.locator('div').filter({ hasText: /^RolCandidato$/ }).first().click();
  await page.getByRole('option', { name: 'Empresa' }).click();
  page.once('dialog', dialog => {
    console.log(`Dialog message: ${dialog.message()}`);
    dialog.dismiss().catch(() => {});
  });
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('jcardonao@uniandes.edu.co');
  page.once('dialog', dialog => {
    console.log(`Dialog message: ${dialog.message()}`);
    dialog.dismiss().catch(() => {});
  });
  await page.getByRole('button', { name: 'Ingresar' }).click();
});

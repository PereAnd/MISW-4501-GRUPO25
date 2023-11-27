import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://bucket-abcjobs-angular.s3-website-us-east-1.amazonaws.com/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('jorge@gmail.com');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Rol').locator('svg').click();
  await page.getByRole('option', { name: 'Empresa' }).click();
  page.once('dialog', dialog => {
    console.log(`Dialog message: ${dialog.message()}`);
    dialog.dismiss().catch(() => {});
  });
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByLabel('Rol').locator('svg').click();
  await page.getByRole('option', { name: 'Candidato' }).click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Información Técnica' }).click();
  await page.getByText('Filtrar').click();
  await page.getByPlaceholder('Escribe algo').fill('');
  await page.getByRole('link', { name: 'Agregar nueva' }).click();
  await page.locator('svg').click();
  await page.getByRole('option', { name: 'Habilidad' }).click();
  await page.getByLabel('Descripción').click();
  await page.getByLabel('Descripción').press('CapsLock');
  await page.getByLabel('Descripción').fill('Trabajo en ');
  await page.getByLabel('Descripción').press('CapsLock');
  await page.getByLabel('Descripción').fill('Trabajo en Equipo');
  await page.getByRole('button', { name: 'Guardar' }).click();
  await page.getByPlaceholder('Escribe algo').click();
  await page.getByPlaceholder('Escribe algo').fill('trabajo');
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

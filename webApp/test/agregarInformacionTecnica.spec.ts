import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('j.cardonao@uniandes.edu.co');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('123456');
  await page.getByRole('link', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Información Técnica' }).click();
  await page.getByRole('link', { name: 'Agregar nueva' }).click();
  await page.getByLabel('Tipo').click();
  await page.getByRole('listbox', { name: 'Tipo' }).click();
  await page.getByText('Descripción').click();
  await page.getByLabel('Descripción').press('CapsLock');
  await page.getByLabel('Descripción').fill('Prueba');
  await page.getByRole('button', { name: 'Guardar' }).click();
  await page.getByRole('link', { name: 'Agregar nueva' }).click();
  await page.getByLabel('Tipo').click();
  await page.getByRole('listbox', { name: 'Tipo' }).click();
  await page.getByText('Descripción').click();
  await page.getByLabel('Descripción').press('CapsLock');
  await page.getByLabel('Descripción').fill('Prueba2');
  await page.getByRole('button', { name: 'Guardar' }).click();
});

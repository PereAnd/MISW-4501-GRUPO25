import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('j.cardonao');
  await page.getByLabel('Correo').press('Alt+@');
  await page.getByLabel('Correo').fill('j.cardonaouniandes.edu.co');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('123456');
  await page.getByRole('link', { name: 'Ingresar' }).click();
  await page.getByRole('link', { name: 'Información Técnica' }).click();
  await page.getByPlaceholder('Escribe algo').click();
  await page.getByPlaceholder('Escribe algo').press('CapsLock');
  await page.getByPlaceholder('Escribe algo').fill('');
  await page.getByLabel('Next page').click();
  await page.getByLabel('Previous page').click();
});

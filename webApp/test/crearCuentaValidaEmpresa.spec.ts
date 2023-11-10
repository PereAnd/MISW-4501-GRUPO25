import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByRole('button', { name: 'Crear cuenta' }).click();
  await page.getByRole('menuitem', { name: 'Empresa' }).click();
  await page.getByText('Nombre Empresa').click();
  await page.getByLabel('Nombre Empresa').press('CapsLock');
  await page.getByLabel('Nombre Empresa').fill('Tecnoweb');
  await page.getByText('Correo').click();
  await page.getByLabel('Correo').fill('tecweb@gmail.com');
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByText('Confirmar contraseña').click();
  await page.getByLabel('Confirmar contraseña').fill('qwerty');
  await page.getByRole('button', { name: 'Crear cuenta' }).click();
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

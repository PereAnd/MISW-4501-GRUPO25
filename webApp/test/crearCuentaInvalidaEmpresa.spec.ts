import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://bucket-abcjobs-angular.s3-website-us-east-1.amazonaws.com/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByRole('button', { name: 'Crear cuenta' }).click();
  await page.getByRole('menuitem', { name: 'Empresa' }).click();
  await page.locator('div').filter({ hasText: /^Crear cuenta$/ }).click();
  await page.getByText('Nombre Empresa').click();
  await page.getByLabel('Nombre Empresa').press('CapsLock');
  await page.getByLabel('Nombre Empresa').fill('Tecweb');
  await page.locator('div').filter({ hasText: /^Crear cuenta$/ }).click();
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill('tecweb@gmail.com');
  await page.locator('div').filter({ hasText: /^Crear cuenta$/ }).click();
  await page.getByLabel('Contraseña', { exact: true }).click();
  await page.getByLabel('Contraseña', { exact: true }).fill('1');
  await page.locator('div').filter({ hasText: /^Crear cuenta$/ }).click();
  await page.getByText('Confirmar contraseña').click();
  await page.getByLabel('Confirmar contraseña').fill('1');
  await page.locator('div').filter({ hasText: /^Crear cuenta$/ }).click();
  await page.getByLabel('Contraseña', { exact: true }).click();
  await page.getByLabel('Contraseña', { exact: true }).fill('123');
  await page.getByLabel('Confirmar contraseña').click();
  await page.getByLabel('Confirmar contraseña').fill('12');
  await page.getByLabel('Nombre Empresa').click();
  await page.getByLabel('Nombre Empresa').fill('');
  await page.locator('div').filter({ hasText: /^Crear cuenta$/ }).click();
});

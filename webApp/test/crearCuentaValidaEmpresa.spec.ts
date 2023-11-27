import { test, expect } from '@playwright/test';
import { faker } from '@faker-js/faker';

test('test', async ({ page }) => {
  await page.goto('http://bucket-abcjobs-angular.s3-website-us-east-1.amazonaws.com/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByRole('button', { name: 'Crear cuenta' }).click();
  await page.getByRole('menuitem', { name: 'Empresa' }).click();
  await page.getByText('Nombre Empresa').click();
  await page.getByLabel('Nombre Empresa').press('CapsLock');
  await page.getByLabel('Nombre Empresa').fill('Tecnoweb');
  await page.getByText('Correo').click();
  await page.getByLabel('Correo').fill(faker.internet.email());
  await page.getByLabel('Correo').press('Tab');
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByText('Confirmar contraseña').click();
  await page.getByLabel('Confirmar contraseña').fill('qwerty');
  await page.getByRole('button', { name: 'Crear cuenta' }).click();
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

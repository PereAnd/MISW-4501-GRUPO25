import { test, expect } from '@playwright/test';
import { faker } from '@faker-js/faker';


test('test', async ({ page }) => {
  await page.goto('http://bucket-abcjobs-angular.s3-website-us-east-1.amazonaws.com/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByRole('button', { name: 'Crear cuenta' }).click();
  await page.getByRole('menuitem', { name: 'Candidato' }).click();
  await page.getByText('Nombres').click();
  await page.getByLabel('Nombres').press('CapsLock');
  await page.getByLabel('Nombres').fill(faker.person.firstName());
  await page.getByText('Apellidos').click();
  await page.getByLabel('Apellidos').press('CapsLock');
  await page.getByLabel('Apellidos').fill(faker.person.lastName());
  await page.getByLabel('Correo').click();
  await page.getByLabel('Correo').fill(faker.internet.email());
  await page.getByText('Contraseña', { exact: true }).click();
  await page.getByLabel('Contraseña', { exact: true }).fill('qwerty');
  await page.getByLabel('Contraseña', { exact: true }).press('Tab');
  await page.getByLabel('Confirmar contraseña').fill('qwerty');
  await page.getByRole('button', { name: 'Crear cuenta' }).click();
  await page.locator('button').filter({ hasText: 'logout' }).click();
});

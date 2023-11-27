import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://bucket-abcjobs-angular.s3-website-us-east-1.amazonaws.com/');
  await page.getByRole('link', { name: 'Servicios' }).click();
  await page.getByRole('link', { name: 'Portafolio' }).click();
  await page.getByRole('link', { name: 'Nosotros' }).click();
  await page.getByRole('link', { name: 'Equipo' }).click();
  await page.getByRole('link', { name: 'Contacto' }).click();
  await page.locator('a').first().click();
});

import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:4200/');
  await page.getByRole('link', { name: 'Servicios' }).click();
  await page.getByRole('link', { name: 'Portafolio' }).click();
  await page.getByRole('link', { name: 'Nosotros' }).click();
  await page.getByRole('link', { name: 'Equipo' }).click();
  await page.getByRole('link', { name: 'Contacto' }).click();
  await page.locator('a').first().click();
});

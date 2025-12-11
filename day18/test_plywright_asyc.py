# test_playwright_async.py
import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.flipkart.com/")
        await expect(page).to_have_url("https://www.flipkart.com/")
        await browser.close()

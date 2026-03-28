"""
Sample Playwright Script with Stealth and Proxy Integration
Author: multilogin-automation
"""
import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

PROXY = "http://username:password@proxyhost:port"
TARGET_URL = "https://bot.sannysoft.com/"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(proxy={"server": PROXY}, headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await stealth_async(page)
        await page.goto(TARGET_URL)
        await page.screenshot(path="stealth_result.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

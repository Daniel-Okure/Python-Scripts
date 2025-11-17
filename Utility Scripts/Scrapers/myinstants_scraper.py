import os
import asyncio
from playwright.async_api import async_playwright

meme_sounds = os.path.join(os.path.expanduser("~"), "Music", "Meme Sounds")

if not os.path.exists(meme_sounds):
    os.mkdir(meme_sounds)

os.chdir(meme_sounds)

async def myinstants_scraper(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        
        await page.goto(url, wait_until="domcontentloaded")
        
        for _ in range(30):
            await page.mouse.wheel(0, 1000)
            await asyncio.sleep(2)
            
        buttons = await page.query_selector_all("button")
        
        for button in buttons:
            onclick = await button.get_attribute("onclick")
            if onclick and onclick.startswith("play"):
                new_str = onclick[6:]
                new_list = new_str.split()
                for item in new_list:
                    if item.startswith("/media"):
                        new_item = item[:-2]
                        link = "https://www.myinstants.com" + new_item
                        filename = os.path.basename(link)
                        link_get = await context.request.get(link)
                        file_content = await link_get.body()
                        
                        with open(filename, "wb") as f:
                            f.write(file_content)
                
    await browser.close()

page_url = "https://www.myinstants.com/en/index/us"
asyncio.run(myinstants_scraper(page_url))
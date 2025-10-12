import asyncio
from playwright.async_api import async_playwright

async def attendance_checker(url, username, password, mode="Lecture Attendance"):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True) # Set to False if you want to see the magic :)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url, wait_until="networkidle", timeout=0)
        
        user = username # Username
        passwd = password # Password
        mode_options = ["Lecture Attendance", "Student Affairs"]
        
        await page.locator("input[name='userid']").fill(user)
        await page.locator("input[name='inputpassword1']").fill(passwd)
        await page.click("input[type='submit']")
        
        await page.click("text=attendance", timeout=0)
        
        # Navigate to the attendance you want to check
        if mode == "Lecture Attendance":
            await page.click("text=Lecture Attendance Reports", timeout=0)
            await page.click("text=Attendance Summay For Student", timeout=0) # lol typo
            
            # Get Lecture Attendance
            frame = page.frame_locator("iframe#frame")
            await frame.locator("div.col-md-10").wait_for(state="visible")
            await frame.locator("div.col-md-10").screenshot(path="lt_attendance.png")
            
        elif mode == "Student Affairs":
            await page.click("text=Student Affairs Attendance", timeout=0)
            await page.click("text=Attendance Summary For Student", timeout=0)
            
            # Get Chapel Attendance
            frame = page.frame_locator("iframe#frame")
            await frame.locator("div#upload-report").wait_for(state="visible")
            await frame.locator("div#upload-report").screenshot(path="chapel_attendance.png")
            
            # Get Roll Call
            await frame.locator("li#event3").click()
            await asyncio.sleep(10) # Waits for the Roll Call to load
            await frame.locator("div#upload-report").screenshot(path="roll_call.png")
            
        elif mode not in mode_options:
            print("Invalid mode: Lecture Attendance or Student Affairs")
        
        await browser.close()
        
portal_url = "https://cuportal.covenantuniversity.edu.ng/login.php"
asyncio.run(attendance_checker(portal_url, "", "")) # Input your username and password here
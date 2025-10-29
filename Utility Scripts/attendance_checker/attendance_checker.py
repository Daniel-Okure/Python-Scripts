import asyncio
import stdiomask
from playwright.async_api import async_playwright

print("Enter your portal username (Reg No): ")
user = input().strip() # Username

passwd = stdiomask.getpass(prompt="Enter your portal password: ", mask="*") # Password

print("What do you want to check: Lecture Attendance (1) or Student Affairs (2)?")
choice = input().strip()

async def attendance_checker(url, username, password, mode):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True) # Set to False if you want to see the magic :)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url, wait_until="networkidle", timeout=0)
        
        mode_options = ["1", "2"]
        
        if mode in mode_options:
            
            await page.locator("input[name='userid']").fill(username)
            await page.locator("input[name='inputpassword1']").fill(password)
            await page.click("input[type='submit']")
            
            error_message = await page.locator("text=Username or Password Incorrect").is_visible()
            
            if error_message:
                password2 = stdiomask.getpass(prompt="Invalid Username or Password. Please re-enter your password: ", mask="*")
                await page.locator("input[name='userid']").fill(username)
                await page.locator("input[name='inputpassword1']").fill(password2)
                await page.click("input[type='submit']")
                await asyncio.sleep(5)
                
            if await page.locator("text=Username or Password Incorrect").is_visible():
                print("Login failed again. Exiting.")
                await browser.close()
                return
            
            print("Successfully logged in! Navigating...")
            await page.click("text=attendance", timeout=0)
        
            # Navigate to the attendance you want to check
            if mode == "1":
                await page.click("text=Lecture Attendance Reports", timeout=0)
                await page.click("text=Attendance Summay For Student", timeout=0) # lol typo
            
                # Get Lecture Attendance
                frame = page.frame_locator("iframe#frame")
                await frame.locator("div.col-md-10").wait_for(state="visible")
                await frame.locator("div.col-md-10").screenshot(path="lt_attendance.png")
            
            elif mode == "2":
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
                
        else:
            print("Invalid mode: Lecture Attendance (1) or Student Affairs (2)")
            
        await browser.close()
        
portal_url = "https://cuportal.covenantuniversity.edu.ng/login.php"
asyncio.run(attendance_checker(portal_url, user, passwd, choice))
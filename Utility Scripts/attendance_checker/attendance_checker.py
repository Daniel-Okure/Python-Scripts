import asyncio
import stdiomask
from pathlib import Path
from playwright.async_api import async_playwright

print("Enter your portal username (Reg No): ")
user = input().strip() # Username

passwd = stdiomask.getpass(prompt="Enter your portal password: ", mask="*") # Password

print("What do you want to check: Lecture Attendance (1) or Student Affairs (2)?")
choice = input().strip()

print("Logging in...")

async def attendance_checker(url, username, password, mode):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled, --disable-infobars"]) # Set to False if you want to see the magic :)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
        )
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
                
                if await frame.locator("div#sub-frame-error").is_visible():
                    print("The page is currently unavailable. Try again at another time. \n\nExiting...")
                    await browser.close()
                else:
                    await frame.locator("div.col-md-10").wait_for(state="visible", timeout=0)
                    await frame.locator("div.col-md-10").screenshot(path="lt_attendance.png")
                    print(f"lt_attendance.png saved to {Path.cwd()}")
                
            
            elif mode == "2":
                await page.click("text=Student Affairs Attendance", timeout=0)
                await page.click("text=Attendance Summary For Student", timeout=0)
            
                frame = page.frame_locator("iframe#frame")
                
                if await frame.locator("div#sub-frame-error").is_visible():
                    print("The page is currently unavailable. Try again at another time. \n\nExiting...")
                    await browser.close()
                
                else:
                    # Get Chapel Attendance
                    await frame.locator("div#upload-report").wait_for(state="visible", timeout=0)
                    await frame.locator("div#upload-report").screenshot(path="chapel_attendance.png")
                    print(f"chapel_attendance.png saved to {Path.cwd()}")
                    
                    # Get Roll Call
                    await frame.locator("li#event3").click()
                    await asyncio.sleep(10)  # Waits for the Roll Call to load
                    await frame.locator("div#upload-report").screenshot(path="roll_call.png")
                    print(f"roll_call.png saved to {Path.cwd()}")
                
                
        else:
            print("Invalid mode: Lecture Attendance (1) or Student Affairs (2)")
            
        await browser.close()
        
portal_url = "https://cuportal.covenantuniversity.edu.ng/login.php"
asyncio.run(attendance_checker(portal_url, user, passwd, choice))
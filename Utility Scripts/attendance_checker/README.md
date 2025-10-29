# Attendance Checker

This is a simple python script I wrote that logs into your portal and checks your attendance based on the arguments you pass to the function. It screenshots these and saves the .png files wherever you run the script. 

---

## Features

- It's simple and easy to use
- Works on Windows, macOS, and Linux
- Saves you the time and stress of checking your attendance yourself 

---

## Requirements
- Python **3.8 or higher**  
- Internet connection (for installing dependencies) and page navigation

---

## Installation Guide

### Step 1: Check if Python is installed

1. Open your **Command Prompt** on Windows
2. Type the following and press **Enter**:
   ```bash
   python --version

If you see something like python 3.10.0, you're good to go! If not, then visit [Python.org](https://www.python.org/downloads/) and install the latest version of python.

### Step 2: Make sure Python and pip are added to PATH (Windows users)

1. During Python installation, make sure to check the box that says *Add Python to PATH*
2. If you forgot to do that, follow these steps:

- Press Windows Key + R, type sysdm.cpl, and hit Enter.

- Go to the Advanced tab → Environment Variables.

- Under System variables, find and select Path → click Edit.

- Click New and add your Python installation paths.

  Example:

```bash
  C:\Users\<YourName>\AppData\Local\Programs\Python\Python311\
```
  
```bash
  C:\Users\<YourName>\AppData\Local\Programs\Python\Python311\Scripts
```


3. Verify installation:
```bash
   python --version
```

### Step 3: For MacOS

1. Like in Windows, first open your **Terminal** and confirm whether you have python already installed
2. Type the following and press **Enter:**
```bash
   python3 --version
```
3. If you don't see anything, visit [Python.org](https://www.python.org/downloads/macos/) and install the latest python release for macOS.

### Step 4: Verify Python and pip installation

After installation, check that both Python and pip work in the command prompt or terminal, with:

```bash
  python --version
``` 
for windows and 

```bash
  python3 --version
``` 
for mac

```bash
  pip --version
``` 
for windows and 

```bash
  pip3 --version
``` 
for mac.

If this doesn't work for you, refer back to step 2 and ensure you add both Python and pip to PATH **(Windows Users)**.

### Step 5: Install project dependencies

Go to your command line **(cmd)** for Windows or **(terminal)** for mac/linux and install playwright and the browser it uses, with:

```bash
  pip install playwright
  pip install stdiomask
``` 
installs playwright and stdiomask modules on windows while 
```bash
  pip3 install playwright
  pip3 install stdiomask
``` 
installs the dependencies on mac.

```bash
  playwright install chromium
``` 
installs the headless browser playwright uses on windows while 
```bash
  python3 -m playwright install chromium
``` 
does the same on mac.

### Step 6: Run the script

It may seem daunting to set up, but once python and all the dependencies are installed, you can double-click the script to run it however many times you want on Windows!

However, to run the script on Mac, users will need to right-click and open the script with Python Launcher. If you see any prompt window pop up, allow the script to access your terminal, and it should run just fine.

From there, all that's left is to input your cuportal username, password, and the attendance you want to check as prompted. 


I tried to make this with poor network conditions in mind, but the bot works best with good connectivity. Otherwise, it may timeout and exit unsuccessfully.



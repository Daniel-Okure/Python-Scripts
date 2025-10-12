# Attendance Checker

This is a simple python script I wrote that logs into your portal and checks your attendance based on the arguments you pass to the function. It screenshots these and saves the .png files wherever you run the script. 

---

## Features

- It's simple and easy to use
- Works on Windows, macOS, and Linux
- More convenient

---

## Requirements
- Python **3.8 or higher**  
- Internet connection (for installing dependencies)

---

## Installation Guide

### Step 1: Check if Python is installed

1. Open your **Command Prompt (Windows)** or **Terminal (macOS/Linux)**.  
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

  ```C:\Users\<YourName>\AppData\Local\Programs\Python\Python311\```
  ```C:\Users\<YourName>\AppData\Local\Programs\Python\Python311\Scripts\```

3. Verify installation:
```python --version```

### Step 3: For MacOS

1. MacOS often includes Python 2 by default. You'll need a newer version.
2. Install [Homebrew](https://brew.sh/) if you don't have it, then run:
```brew install python```
3. Verify installation:
```python --version```

### Step 4: Verify Python and pip installation

After installation, check that both Python and pip work, with:

```python --version``` for python

```pip --version``` for pip

If they don't work, refer back to step 2 and ensure you add both Python and pip to PATH.

### Step 5: Install project dependencies

Go to your command line **(cmd)** for Windows **(terminal)** for mac/linux and install playwright and the browser it uses, with:

```pip install playwright``` installs the playwright module

```playwright install``` installs the chromium browser

### Step 6: Run the script

Open the code editor of your choice or python's IDLE and input your cuportal username and password to the attendance checker function as directed in the comments. 

Lecture Attendance is set by default, but if you want to check your chapel and roll call, set the mode parameter to Student Affairs and run the script.

I tried to make this with poor network conditions in mind (that's why there are so many timeouts), but the bot works best with good connectivity. Otherwise, it may timeout and exit unsuccessfully.



# Module 1: Setup & First Script

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Install Python and Cursor or Visual Studio Code
- Create your first Python script
- Understand what Python is in simple terms
- Write and run a program that displays messages using `python hello.py`
- Use the integrated terminal in Cursor or VS Code
- **Build something real:** A simple program that greets you and can be customized

## 🌍 Real-World Connection

Think of this like learning to use a new tool at work. Before you can build anything impressive, you need to:
1. Install the tool
2. Learn the basics of how it works
3. Make your first small thing with it

That's exactly what we're doing here. By the end, you'll have created a tiny program that talks to you - and that's your first step toward building tools that solve real problems.

## 📖 What is Python? (In Plain English)

**Python** is a programming language - a way to write instructions that computers can understand. Think of it like learning a new language to communicate with computers.

**Why Python?**
- **Easy to learn** - Clear, readable syntax (like plain English)
- **Very popular** - Used by Google, Netflix, Instagram, NASA, and thousands of companies
- **Versatile** - Can build websites, analyze data, automate tasks, create games
- **Great job opportunities** - High demand for Python developers
- **Free and open** - No cost, huge community support

**Real-world uses:**
- **Web development** - Building websites and web applications
- **Data analysis** - Working with spreadsheets, databases, and data
- **Automation** - Automating repetitive tasks
- **Machine learning** - AI and data science projects
- **Scripting** - Quick tools and utilities

## 🛠️ Step 1: Installing Python

Python is free and available for Windows, macOS, and Linux.

### For Windows:

1. **Open your web browser**
2. **Go to:** https://www.python.org/downloads/
3. **Click the big yellow "Download Python" button** (get the latest version, usually 3.11 or newer)
4. **Run the installer file** you downloaded
5. **IMPORTANT:** Check the box that says **"Add Python to PATH"** at the bottom of the installer window
   - This lets you run Python from anywhere
6. **Click "Install Now"**
7. **Wait for installation** (usually takes 1-2 minutes)
8. **When it says "Setup was successful," click "Close"**

### For macOS:

1. **Open your web browser**
2. **Go to:** https://www.python.org/downloads/
3. **Click "Download Python" for macOS**
4. **Open the downloaded .pkg file**
5. **Follow the installation steps** (click "Continue" through the steps)
6. **Click "Install"** when prompted
7. **Enter your password** if asked

### For Linux:

Most Linux systems come with Python pre-installed. To check:
1. Open a terminal
2. Type: `python3 --version`
3. If you see a version number (like `Python 3.11.0`), you're good!
4. If not, install with: `sudo apt install python3` (Ubuntu/Debian) or `sudo yum install python3` (Red Hat)

### Verify Installation:

1. **Open a terminal/command prompt:**
   - **Windows:** Press `Win + R`, type `cmd`, press Enter
   - **macOS:** Press `Cmd + Space`, type "Terminal", press Enter
   - **Linux:** Press `Ctrl + Alt + T` or find Terminal in your applications

2. **Type this command and press Enter:**
   ```
   python --version
   ```
   (On Mac/Linux, you might need to use `python3 --version` instead)

3. **You should see a version number** (like `Python 3.11.5`). If you see an error, the installation didn't work - try installing again.

**✅ Checkpoint:** Can you see a version number? Great! Move to Step 2.

## 🛠️ Step 2: Installing Cursor or Visual Studio Code

You need a code editor to write and edit your Python programs. You can use either **Cursor** or **Visual Studio Code** - both work great!

### Option A: Cursor (Recommended)

Cursor is a modern code editor built for AI-assisted coding.

1. **Go to:** https://cursor.sh
2. **Download and install Cursor**
3. **Open Cursor** after installation
4. **Install the Python extension:**
   - Click the Extensions icon (left sidebar, looks like four squares)
   - Search for "Python" (by Microsoft)
   - Click "Install"

### Option B: Visual Studio Code

Visual Studio Code (VS Code) is a free, popular code editor.

1. **Go to:** https://code.visualstudio.com/
2. **Download and install VS Code**
3. **Open VS Code** after installation
4. **Install the Python extension:**
   - Click the Extensions icon (left sidebar)
   - Search for "Python" (by Microsoft)
   - Click "Install"

**✅ Checkpoint:** Can you open Cursor or VS Code? Is the Python extension installed? Great! Move to Step 3.

## 🛠️ Step 3: Creating Your First Python Script

Now we'll create your first Python program. Think of a Python script as a text file with instructions that Python can run.

### Step-by-Step Instructions:

1. **Open Cursor or VS Code**

2. **Open the Integrated Terminal:**
   - Click `Terminal` in the top menu
   - Then click `New Terminal`
   - OR press `` Ctrl + ` `` (that's Ctrl + backtick, the key above Tab)
   - You should see a terminal window appear at the bottom

3. **Navigate to where you want your projects:**
   - In the terminal, type:
     ```
     cd Desktop
     ```
   - Press Enter
   - (Or use `cd Documents` if you prefer to keep projects in Documents)

4. **Create a new folder for this workbook:**
   ```
   mkdir PythonLearning
   cd PythonLearning
   ```

5. **Create your first Python file:**
   - Click "New File" button or press `Ctrl + N` (Windows) / `Cmd + N` (Mac)
   - Type: `print("Hello, World!")`
   - Save the file: Press `Ctrl + S` (Windows) / `Cmd + S` (Mac)
   - Name it `hello.py` (make sure it ends with `.py` - that's the Python file extension)

**✅ Checkpoint:** Can you see a file called `hello.py` in the left sidebar? Great! Move to Step 4.

## 📝 Step 4: Understanding Your First Program

Let's look at what you just created. Click on `hello.py` in the left sidebar to open it.

You should see something like this:

```python
print("Hello, World!")
```

Let's break this down in simple terms:

- `print` - This is a function (a built-in command) that displays text on the screen
- `("Hello, World!")` - This is the text we want to display (the quotes tell Python this is text)
- The parentheses `()` - These tell Python to "run" or "call" the print function

**Think of it like:** You're telling the computer: "Hey, print this message to the screen."

**Note:** Unlike some languages, Python doesn't need semicolons at the end of lines. Python uses line breaks instead!

## 🚀 Step 5: Running Your First Program

Now let's make your program run!

1. **Make sure the terminal is open** (if not, press `` Ctrl + ` ``)

2. **Make sure you're in the right folder:**
   - You should see `PythonLearning` in your terminal prompt
   - If not, type: `cd PythonLearning`

3. **Run your program:**
   ```
   python hello.py
   ```
   (On Mac/Linux, you might need to use `python3 hello.py` instead)

4. **You should see:**
   ```
   Hello, World!
   ```

**🎉 Congratulations!** You just ran your first Python program!

### What Just Happened?

- `python hello.py` tells Python to:
  1. Read the file `hello.py`
  2. Execute the instructions in it
  3. Show you the output

Think of it like giving Python a recipe (your `.py` file) and asking it to follow it.

## ✏️ Step 6: Making It Your Own

Let's modify the program to make it more personal:

1. **Change the message in `hello.py`:**
   Replace the line with:
   ```python
   print("Hello! My name is [Your Name]")
   ```
   (Replace `[Your Name]` with your actual name)

2. **Add another line:**
   Add this below the first line:
   ```python
   print("This is my first Python program!")
   ```

3. **Save the file:**
   - Press `Ctrl + S` (Windows/Linux) or `Cmd + S` (macOS)
   - Or click `File > Save`

4. **Run it again:**
   ```
   python hello.py
   ```

5. **You should see both messages!**

**Your `hello.py` should now look like:**
```python
print("Hello! My name is [Your Name]")
print("This is my first Python program!")
```

## 🔍 Step 7: Using the Debugger (Optional but Helpful)

The debugger lets you pause your program and see what's happening step by step. This is incredibly useful when things go wrong.

### Setting a Breakpoint:

1. **Click in the left margin** next to a line of code (you'll see a red dot appear)
   - Try clicking next to `print("Hello! My name is...");`

2. **Start debugging:**
   - **In Cursor or VS Code:** Press `F5` OR
   - Click the Run and Debug icon on the left sidebar (play button with bug)
   - Click "Run and Debug" button
   - Select "Python File" if prompted

3. **Your program will pause** at the red dot (breakpoint)

4. **Inspect what's happening:**
   - Look at the left side - you'll see variables and other information
   - At the top, you'll see buttons:
     - **Continue (F5)** - Run until next breakpoint
     - **Step Over (F10)** - Execute the current line and move to next
     - **Stop** - Stop debugging

5. **Press F10** to step through your code line by line

6. **Press F5** to continue running normally

**Why this matters:** When your programs get more complex, breakpoints help you find bugs and understand what's happening.

## 📚 Key Concepts You've Learned

1. **Python Script** - A text file with `.py` extension containing Python code
2. **print()** - A function that displays text on the screen
3. **String** - Text wrapped in quotes (like `"Hello"`)
4. **Running** - Executing your program with `python hello.py`
5. **Terminal** - The command-line interface where you run programs

## 🎓 Exercises

Now it's time to practice! Try these exercises to build your confidence.

### Exercise 1: Personal Greeting Program

**Task:** Create a program that greets you and tells you something about yourself.

**Steps:**
1. Create a new file called `greeting.py`
2. Write code to print:
   - Your name
   - Your favorite hobby or interest
   - One thing you hope to learn from this course

**Example output:**
```
Hello! I'm Sarah.
I love reading science fiction books.
I hope to learn how to build useful tools with code.
```

**Try it yourself first!** Then check the solution in `exercises/exercise-01-solution.md`.

---

### Exercise 2: Multi-Line Message

**Task:** Create a program that prints a short story or message across multiple lines.

**Steps:**
1. Create a new file called `story.py`
2. Write at least 3 `print()` statements
3. Each should print a different line of your story

**Example output:**
```
Today is a great day to learn Python!
I'm excited to start this journey.
Let's build something amazing together!
```

**Try it yourself first!** Then check the solution in `exercises/exercise-02-solution.md`.

---

### Exercise 3: Predict the Output

**Task:** Look at this code and predict what it will output BEFORE running it:

```python
print("First line")
print("Second line")
print("Third line")
```

**Your prediction:** Write down what you think will happen.

**Now run it:** Create a file called `predict.py`, paste the code, and run it.

**Were you right?** Understanding what code does before running it is an important skill!

---

## 🐛 Debug Challenge

Here's some broken code. Can you find and fix the errors?

```python
print("Hello World)
print("This is Python")
print('I'm learning to code')
```

**Errors to find:**
1. Missing closing quote
2. Missing closing quote
3. Quote conflict (single quote inside single quotes)

**Try fixing it yourself!** Then check `exercises/debug-challenge-solution.md` for the solution.

## 🧪 Mini Quiz

Test your understanding with these questions:

### Question 1: What does `print()` do?
A) Reads input from the user  
B) Displays text on the screen  
C) Saves data to a file  
D) Calculates numbers

**Answer:** B - `print()` displays text on the screen

---

### Question 2: What file extension do Python files use?
A) `.txt`  
B) `.py`  
C) `.python`  
D) `.exe`

**Answer:** B - Python files use `.py` extension

---

### Question 3: How do you run a Python file called `hello.py`?
A) `run hello.py`  
B) `python hello.py`  
C) `execute hello.py`  
D) `start hello.py`

**Answer:** B - Use `python hello.py` (or `python3 hello.py` on Mac/Linux)

---

### Question 4: True or False: Python needs semicolons at the end of each line.
A) True  
B) False

**Answer:** False - Python uses line breaks instead of semicolons

---

### Question 5: What is Python?
A) A type of snake  
B) A programming language  
C) A code editor  
D) An operating system

**Answer:** B - Python is a programming language

---

**Check your answers:** See `exercises/quiz-answers.md` for explanations.

## 🎉 What's Next?

Congratulations! You've completed Module 1. You can now:
- ✅ Install Python and a code editor
- ✅ Create and run Python scripts
- ✅ Use `print()` to display messages
- ✅ Understand basic Python syntax

**Next up:** Module 2 - Python Basics
- Learn about variables (storing data)
- Get input from users
- Do calculations
- Format strings beautifully

You're ready to move forward! 🚀

---

**Remember:** Every expert was once a beginner. You just wrote and ran your first Python program - that's a huge achievement! Keep going! 💪


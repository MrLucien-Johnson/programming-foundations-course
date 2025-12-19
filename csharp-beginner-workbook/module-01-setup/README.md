# Module 1: Setup & First Program

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Install the .NET SDK and Cursor or Visual Studio Code
- Create your first C# project with `dotnet new console`
- Understand what C# and .NET are in simple terms
- Write and run a program that displays messages using `dotnet run`
- Use the integrated terminal in Cursor or VS Code
- **Build something real:** A simple program that greets you and can be customized

## 🌍 Real-World Connection

Think of this like learning to use a new tool at work. Before you can build anything impressive, you need to:
1. Install the tool
2. Learn the basics of how it works
3. Make your first small thing with it

That's exactly what we're doing here. By the end, you'll have created a tiny program that talks to you - and that's your first step toward building tools that solve real problems.

## 📖 What is C# and .NET? (In Plain English)

**C#** (pronounced "C sharp") is a programming language - a way to write instructions that computers can understand. Think of it like learning a new language to communicate with computers.

**.NET** (pronounced "dot net") is a platform - think of it as a toolbox that gives C# programs everything they need to run. It's like the engine in a car - you don't see it, but it makes everything work.

**Why C#?**
- Used by many companies (Microsoft, banks, game companies, and more)
- Great for building tools, websites, and applications
- Good job opportunities
- Clear and readable code (easier to learn than some languages)

## 🛠️ Step 1: Installing .NET SDK

The .NET SDK (Software Development Kit) is like a toolkit that lets you create and run C# programs.

### For Windows:

1. Open your web browser
2. Go to: https://dotnet.microsoft.com/download
3. Click the big "Download .NET SDK" button (get the latest version, usually 8.0 or newer)
4. Run the installer file you downloaded
5. Follow the installation wizard (just click "Next" through the steps)
6. When it says "Installation complete," click "Finish"

### For macOS:

1. Open your web browser
2. Go to: https://dotnet.microsoft.com/download
3. Click "Download .NET SDK" for macOS
4. Open the downloaded .pkg file
5. Follow the installation steps
6. Click "Install" when prompted

### For Linux:

1. Open a terminal
2. Follow the instructions at: https://dotnet.microsoft.com/download/linux
3. Or use your package manager (e.g., `sudo apt install dotnet-sdk-8.0` on Ubuntu)

### Verify Installation:

1. Open a terminal/command prompt:
   - **Windows:** Press `Win + R`, type `cmd`, press Enter
   - **macOS:** Press `Cmd + Space`, type "Terminal", press Enter
   - **Linux:** Press `Ctrl + Alt + T` or find Terminal in your applications

2. Type this command and press Enter:
   ```
   dotnet --version
   ```

3. You should see a version number (like `8.0.100`). If you see an error, the installation didn't work - try installing again.

**✅ Checkpoint:** Can you see a version number? Great! Move to Step 2.

## 🛠️ Step 2: Installing Cursor or Visual Studio Code

You need a code editor to write and edit your C# programs. You can use either **Cursor** or **Visual Studio Code** - both work great!

### Option A: Cursor (Recommended)

Cursor is a modern code editor built for AI-assisted coding.

1. Go to: https://cursor.sh
2. Download and install Cursor
3. Open Cursor after installation
4. Install the C# extension:
   - Click the Extensions icon (left sidebar)
   - Search for "C# Dev Kit"
   - Click "Install"

### Option B: Visual Studio Code

Visual Studio Code (VS Code) is a free, popular code editor.

1. Go to: https://code.visualstudio.com/
2. Download and install VS Code
3. Open VS Code after installation
4. Install the C# extension:
   - Click the Extensions icon (left sidebar)
   - Search for "C# Dev Kit"
   - Click "Install"

**✅ Checkpoint:** Can you open Cursor or VS Code? Is C# Dev Kit installed? Great! Move to Step 3.

## 🛠️ Step 3: Creating Your First Project

Now we'll create your first C# program. Think of a project as a folder that contains everything your program needs.

### Step-by-Step Instructions:

1. **Open VS Code**

2. **Open the Integrated Terminal:**
   - Click `Terminal` in the top menu
   - Then click `New Terminal`
   - OR press `` Ctrl + ` `` (that's Ctrl + backtick, the key above Tab)
   - You should see a terminal window appear at the bottom of VS Code

3. **Navigate to where you want your projects:**
   - In the terminal, type:
     ```
     cd Desktop
     ```
   - Press Enter
   - (Or use `cd Documents` if you prefer to keep projects in Documents)

4. **Create a new folder for this workbook:**
   ```
   mkdir BeginnersCSharp
   cd BeginnersCSharp
   ```

5. **Create your first project:**
   ```
   dotnet new console -n HelloWorld
   ```
   - This creates a new console application (a program that runs in the terminal)
   - The `-n HelloWorld` part names your project "HelloWorld"

6. **Open the project folder in Cursor or VS Code:**
   ```
   cd HelloWorld
   ```
   - **In Cursor:** Use `File > Open Folder` and select the HelloWorld folder
   - **In VS Code:** Type `code .` OR use `File > Open Folder` and select the HelloWorld folder

**✅ Checkpoint:** Can you see a file called `Program.cs` in the left sidebar? Great! Move to Step 4.

## 📝 Step 4: Understanding Your First Program

Let's look at what was created for you. Click on `Program.cs` in the left sidebar to open it.

You should see something like this:

```csharp
// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
```

Let's break this down in simple terms:

- `Console.WriteLine` - This is a command that prints text to the screen
- `"Hello, World!"` - This is the text we want to print (the quotes tell C# this is text)
- The semicolon `;` - This tells C# "this command is finished"

**Think of it like:** You're telling the computer: "Hey, write this message to the screen."

## 🚀 Step 5: Running Your First Program

Now let's make your program run!

1. **Make sure the terminal is open** (if not, press `` Ctrl + ` ``)

2. **Run your program:**
   ```
   dotnet run
   ```

3. **You should see:**
   ```
   Hello, World!
   ```

**🎉 Congratulations!** You just ran your first C# program!

### What Just Happened?

- `dotnet run` tells the .NET tools to:
  1. Compile your code (turn it into something the computer can run)
  2. Run the program
  3. Show you the output

Think of compiling like translating your instructions into a language the computer understands.

## ✏️ Step 6: Making It Your Own

Let's modify the program to make it more personal:

1. **Change the message in `Program.cs`:**
   Replace the line with:
   ```csharp
   Console.WriteLine("Hello! My name is [Your Name]");
   ```
   (Replace `[Your Name]` with your actual name)

2. **Add another line:**
   Add this below the first line:
   ```csharp
   Console.WriteLine("This is my first C# program!");
   ```

3. **Save the file:**
   - Press `Ctrl + S` (Windows/Linux) or `Cmd + S` (macOS)
   - Or click `File > Save`

4. **Run it again:**
   ```
   dotnet run
   ```

5. **You should see both messages!**

**Your `Program.cs` should now look like:**
```csharp
Console.WriteLine("Hello! My name is [Your Name]");
Console.WriteLine("This is my first C# program!");
```

## 🔍 Step 7: Using the Debugger (Optional but Helpful)

The debugger lets you pause your program and see what's happening step by step. This is incredibly useful when things go wrong.

### Setting a Breakpoint:

1. **Click in the left margin** next to a line of code (you'll see a red dot appear)
   - Try clicking next to `Console.WriteLine("Hello! My name is...");`

2. **Start debugging:**
   - **In Cursor or VS Code:** Press `F5` OR
   - Click the Run and Debug icon on the left sidebar (play button with bug)
   - Click "Run and Debug" button
   - Select ".NET 5+ and .NET Core" if prompted

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

1. **Console Application** - A program that runs in the terminal/command prompt
2. **Console.WriteLine** - A command that prints text to the screen
3. **String** - Text wrapped in quotes (like `"Hello"`)
4. **Compiling** - Converting your code into something the computer can run
5. **Running** - Executing your program with `dotnet run`

## 🎓 Exercises

Now it's time to practice! Try these exercises to build your confidence.

### Exercise 1: Personal Greeting Program

**Task:** Create a program that greets you and tells you something about yourself.

**Steps:**
1. Modify `Program.cs` to print:
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
1. Use multiple `Console.WriteLine` statements
2. Print at least 4 lines
3. Make it about something work-related (like a daily task list or a simple announcement)

**Example idea:** A simple daily task reminder
```
Today's Tasks:
1. Review project requirements
2. Attend team meeting at 2 PM
3. Complete Module 1 exercises
4. Plan tomorrow's work
```

**Try it yourself first!** Then check the solution in `exercises/exercise-02-solution.md`.

---

### Exercise 3: Predict the Output

**Task:** Look at this code and predict what it will print. Then type it and run it to check.

```csharp
Console.WriteLine("First line");
Console.WriteLine("Second line");
Console.WriteLine("Third line");
Console.WriteLine("First line");
```

**Questions:**
1. How many lines will be printed?
2. Will "First line" appear twice?
3. What order will they appear in?

**Write your predictions here:**
- Prediction 1: _______________
- Prediction 2: _______________
- Prediction 3: _______________

**Now run it and see if you were right!**

---

## 🧪 Quiz: Test Your Understanding

Answer these questions to check what you've learned. Answers are at the bottom of this file.

### Question 1: What does `Console.WriteLine` do?
A) Reads text from the user  
B) Prints text to the screen  
C) Saves text to a file  
D) Deletes text from the screen

### Question 2: What command do you use to run a C# program?
A) `dotnet start`  
B) `dotnet run`  
C) `dotnet execute`  
D) `run program`

### Question 3: What is a breakpoint used for?
A) To stop your program permanently  
B) To pause your program so you can inspect what's happening  
C) To make your program run faster  
D) To delete code

### Question 4: What does compiling mean?
A) Running your program  
B) Converting your code into something the computer can run  
C) Saving your file  
D) Testing your code

### Question 5: In C#, text that you want to print must be wrapped in:
A) Parentheses `()`  
B) Square brackets `[]`  
C) Quotes `""`  
D) Curly braces `{}`

---

## 🐛 Debug Challenge: Find the Errors

Look at this code. There are 3 mistakes. Can you find them?

```csharp
Console.WriteLine("Welcome to my program")
Console.WriteLine("This is line 2";
Console.Writeline("This is line 3");
```

**Try to find the errors before looking at the solution!**

**Hints:**
- Check punctuation
- Check spelling
- Check quotes

**Solution:** See `exercises/debug-challenge-solution.md`

---

## ✅ Module 1 Checklist

Before moving to Module 2, make sure you can:
- [ ] Install .NET SDK and verify it works
- [ ] Install VS Code and the C# extension
- [ ] Create a new project using `dotnet new console`
- [ ] Open the integrated terminal in VS Code
- [ ] Modify `Program.cs` and run it with `dotnet run`
- [ ] Set a breakpoint and use the debugger (optional but recommended)
- [ ] Complete at least 2 exercises
- [ ] Answer the quiz questions correctly

---

## 🎯 What's Next?

In Module 2, you'll learn about:
- Variables (storing information)
- Different types of data (numbers, text, true/false)
- Getting input from users
- Doing calculations
- Building a price calculator with tax

**Real-world connection:** You'll build tools that can calculate prices, process user information, and make decisions based on data.

---

## 📝 Quiz Answers

1. **B** - `Console.WriteLine` prints text to the screen
2. **B** - `dotnet run` is the command to run a C# program
3. **B** - A breakpoint pauses your program so you can inspect what's happening
4. **B** - Compiling converts your code into something the computer can run
5. **C** - Text must be wrapped in quotes `""`

---

## 💡 Tips for Success

- **Type code yourself** - Don't copy-paste. Typing helps your brain learn.
- **Make mistakes** - Errors are normal! They teach you how things work.
- **Experiment** - Try changing things and see what happens.
- **Take breaks** - Learning to code is like learning a new language. Your brain needs rest.
- **Ask questions** - If something doesn't make sense, that's okay! Keep trying.

---

**Congratulations on completing Module 1!** 🎉

You've taken your first steps toward becoming a skilled C# developer. In the next module, you'll learn how to store and work with information in your programs.

---

## 🔗 Navigation

- **[Next: Module 2 - C# Basics →](../module-02-basics/README.md)**
- **[Back to C# Workbook →](../README.md)**
- **[Back to Course Home →](../../README.md)**
- **[Course Links →](../../COURSE-LINKS.md)**
- **[Examples →](examples/)** | **[Exercises →](exercises/)**


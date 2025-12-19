# Quick Start: Your First C# Program in 5 Minutes

This guide gets you running your first C# program quickly. For detailed instructions, see Module 1.

## ⚡ Step 1: Install .NET SDK

1. Go to https://dotnet.microsoft.com/download
2. Download and install the .NET SDK (latest version)
3. Open a terminal and verify: `dotnet --version`
4. You should see a version number ✅

## ⚡ Step 2: Install Cursor or VS Code

**Option A: Cursor** (Recommended)
- Download from https://cursor.sh
- Install and open Cursor

**Option B: Visual Studio Code**
- Download from https://code.visualstudio.com/
- Install and open VS Code

Then install the **C# Dev Kit** extension:
- Click Extensions icon (left sidebar)
- Search "C# Dev Kit"
- Click Install

## ⚡ Step 3: Create and Run Your First Program

1. **Open Cursor or VS Code**

2. **Open the integrated terminal:**
   - Press `` Ctrl + ` `` (backtick key)
   - Or: `Terminal > New Terminal`

3. **Create a new project:**
   ```bash
   dotnet new console -o HelloWorld
   cd HelloWorld
   ```

4. **Run it:**
   ```bash
   dotnet run
   ```

5. **You should see:** `Hello, World!` ✅

## 🎉 Success!

You just created and ran your first C# program! 

**Next steps:**
- Open `module-01-setup/README.md` for the full lesson
- Learn how to modify and customize your program
- Complete exercises to build confidence

---

**Troubleshooting:**
- If `dotnet` isn't found: Restart your terminal after installing .NET SDK
- If terminal doesn't open: Use `View > Terminal` menu
- Need help? See Module 1 for detailed instructions

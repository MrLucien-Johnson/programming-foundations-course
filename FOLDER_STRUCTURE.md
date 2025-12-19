# Workbook Folder Structure

This document describes the complete folder structure of the C# Beginner's Workbook.

```
BeginnersCSharp/
│
├── README.md                          # Main workbook introduction and table of contents
├── QUICK_START.md                     # 5-minute quick start guide
├── FOLDER_STRUCTURE.md                # This file - explains the structure
├── WORKBOOK_SUMMARY.md                # Summary of the workbook and learning journey
│
├── module-01-setup/                   # Module 1: Setup & First Program (FULL LESSON)
│   ├── README.md                      # Complete detailed lesson content
│   ├── example-01-basic.cs           # Basic Console.WriteLine example
│   ├── example-02-multiple-lines.cs  # Multiple lines example
│   ├── example-03-formatted-output.cs # Formatted output example
│   └── exercises/
│       ├── README.md                  # Exercises introduction
│       ├── exercise-01-solution.md    # Solution to Exercise 1
│       ├── exercise-02-solution.md    # Solution to Exercise 2
│       ├── exercise-03-solution.md   # Solution to Exercise 3
│       ├── debug-challenge-solution.md # Debug challenge solution
│       └── quiz-answers.md            # Answers to Module 1 quiz
│
├── module-02-basics/                  # Module 2: C# Basics (OUTLINE)
│   └── README.md                      # Lesson outline (to be expanded)
│
├── module-03-control-flow/            # Module 3: Control Flow (OUTLINE)
│   └── README.md                      # Lesson outline (to be expanded)
│
├── module-04-methods/                 # Module 4: Methods (OUTLINE)
│   └── README.md                      # Lesson outline (to be expanded)
│
├── module-05-collections/             # Module 5: Collections (OUTLINE)
│   └── README.md                      # Lesson outline (to be expanded)
│
├── module-06-oop-intro/              # Module 6: Intro to OOP (OUTLINE)
│   └── README.md                      # Lesson outline (to be expanded)
│
└── module-07-task-tracker/            # Module 7: Mini Project (OUTLINE)
    └── README.md                      # Project outline (to be expanded)
```

## File Descriptions

### Root Level Files

- **README.md** - Main entry point with table of contents, overview, and learning path
- **QUICK_START.md** - Very short 5-minute guide to get your first program running
- **FOLDER_STRUCTURE.md** - This file, explains the organization
- **WORKBOOK_SUMMARY.md** - Describes the workbook purpose, audience, and learning journey

### Module Structure

**Module 1 (Complete):**
- **README.md** - Full detailed lesson with:
  - Step-by-step installation instructions
  - Plain English explanations of C# and .NET
  - Instructions for using Cursor or VS Code
  - Detailed `dotnet` CLI usage
  - Exercises, quizzes, and debug challenges
  - Real-world connections throughout
- **example-*.cs** - Example code files learners can study
- **exercises/** - Solutions to all exercises and quizzes

**Modules 2-7 (Outlines):**
- **README.md** - Detailed outline containing:
  - Learning objectives
  - Real-world connections
  - Key concepts overview
  - Planned exercises (4-5 per module)
  - Planned quiz questions
  - Planned debug challenges
  - Module checklists
  - Next module previews

## How to Use This Structure

1. **Start with README.md** - Read the main workbook introduction
2. **Try QUICK_START.md** - Get your first program running in 5 minutes
3. **Work through Module 1** - Complete detailed lesson with exercises
4. **Follow modules in order** - Modules 2-7 build on previous knowledge
5. **Read each module's README.md** - Contains all lesson content (full for Module 1, outlines for 2-7)
6. **Try the exercises** - Practice in your own project folders
7. **Check solutions** - Compare your work with provided solutions (Module 1)

## Creating Your Own Projects

For each module, you'll create your own projects using:

```bash
dotnet new console -o ProjectName
cd ProjectName
```

These projects should be created in a separate folder (like `my-projects/` on your Desktop) or in a dedicated workspace folder, **not inside the workbook folders**.

The workbook folders contain:
- Lesson content (README.md files)
- Example code to study
- Exercise solutions to check your work

Your actual coding practice happens in separate project folders you create.

## Notes

- **Module 1** is fully complete with all content, exercises, solutions, and examples
- **Modules 2-7** contain detailed outlines ready to be expanded into full lessons
- All modules follow the same structure for consistency
- Solutions are provided separately so learners can attempt exercises first
- The workbook is designed to be used in **Cursor or Visual Studio Code**
- All projects use the **dotnet CLI** (`dotnet new console`, `dotnet run`)

## Expansion Plan

Modules 2-7 can be expanded following the Module 1 pattern:
- Full step-by-step instructions
- Detailed code examples
- Complete exercise solutions
- Additional example files
- Expanded quiz content

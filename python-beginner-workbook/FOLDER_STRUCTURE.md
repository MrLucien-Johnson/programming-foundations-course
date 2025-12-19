# Workbook Folder Structure

This document explains how the Python Beginner's Workbook is organized.

## 📁 Root Level

```
python-beginner-workbook/
├── README.md                    # Main overview and table of contents
├── QUICK_START.md               # 5-minute quick start guide
├── FOLDER_STRUCTURE.md         # This file - explains the structure
├── WORKBOOK_SUMMARY.md          # Summary of the learning journey
│
├── module-01-setup/             # Module 1: Setup & First Script
├── module-02-basics/            # Module 2: Variables, Input, Calculations
├── module-03-control-flow/      # Module 3: If/Else, Loops
├── module-04-functions/         # Module 4: Functions
├── module-05-collections/        # Module 5: Lists & Dictionaries
├── module-06-oop/               # Module 6: Classes & Objects
└── module-07-task-tracker/      # Module 7: Task Tracker Project
```

## 📚 Each Module Folder Structure

Every module follows the same structure:

```
module-XX-name/
├── README.md                    # Main lesson content
├── examples/                    # Sample code files
│   ├── example-01-name.py
│   ├── example-02-name.py
│   └── example-03-name.py
├── exercises/                  # Practice exercises
│   ├── README.md               # How to use exercises
│   ├── exercise-01.md          # Exercise instructions
│   ├── exercise-02.md
│   ├── exercise-03.md
│   ├── debug-challenge.md      # Find the errors challenge
│   ├── quiz.md                 # Self-test questions
│   ├── exercise-01-solution.md # Solutions
│   ├── exercise-02-solution.md
│   ├── exercise-03-solution.md
│   ├── debug-challenge-solution.md
│   └── quiz-answers.md         # Quiz answers
└── solutions/                   # Additional solution files (if needed)
```

## 📖 What Each File Type Does

### README.md (in each module)
- The main lesson content
- Step-by-step instructions
- Explanations of concepts
- Code examples embedded in the lesson
- Links to example files and exercises

### examples/ Folder
- Working Python code files (`.py`)
- Can be run directly: `python example-01-name.py`
- Demonstrates concepts from the lesson
- Study these to understand how code works

### exercises/ Folder
- **Exercise files** (`.md`): Instructions for practice problems
- **Solution files** (`*-solution.md`): Answers to check your work
- **Quiz** (`quiz.md`): Test your understanding
- **Debug challenge**: Find and fix errors in broken code

### How to Use Exercises

1. **Read the lesson** (`README.md`) first
2. **Study the examples** in `examples/` folder
3. **Try the exercises** - read `exercise-01.md`, write your code, test it
4. **Check solutions** - compare with `exercise-01-solution.md`
5. **Take the quiz** - test your understanding
6. **Try the debug challenge** - practice finding errors

## 🎯 Module 7 Special Structure

Module 7 (Task Tracker) includes:
- `README.md` - Full project guide
- `project/` - Complete working application
  - `task_item.py`
  - `task_manager.py`
  - `main.py`
- `exercises/` - Enhancement challenges
- `solutions/` - Solutions to challenges

## 💡 Tips for Navigation

- **Start with Module 1** - Work through modules in order
- **Read README.md first** - It contains the main lesson
- **Run example files** - See code in action
- **Do exercises** - Practice makes perfect
- **Check solutions** - Learn from different approaches

## 🔍 Finding What You Need

- **Want to learn a concept?** → Read the module's `README.md`
- **Want to see working code?** → Check `examples/` folder
- **Want to practice?** → Try exercises in `exercises/` folder
- **Stuck on an exercise?** → Check the solution file
- **Want to test yourself?** → Take the quiz

---

**Remember:** This structure is designed to help you learn step by step. Take your time and work through each module thoroughly!


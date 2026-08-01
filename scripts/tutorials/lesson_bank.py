"""Additional teaching voiceover lessons for beginner modules + advanced orientation."""

# Appended to TUTORIALS in generate_tutorials.py

EXTRA_TUTORIALS = [
    {
        "id": "09-python-control-flow",
        "title": "Python Module 3 — decisions & loops lesson",
        "kind": "lesson",
        "when": "python-course, module-03-control-flow",
        "footer": "tutorials.html · Python Module 3",
        "pathMatch": "python-beginner-workbook/module-03-control-flow",
        "hubAnchor": "python-control-flow",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Make decisions with if, elif, and else",
                    "Compare values and combine conditions",
                    "Repeat work with for and while loops",
                ],
                "vo": "Today’s lesson goal: make decisions with if, elif, and else, compare values and combine conditions, and repeat work with for and while loops.",
            },
            {
                "title": "Why control flow matters",
                "bullets": [
                    "Programs choose paths — discounts, menus, checks",
                    "Loops process lists without copy-paste",
                    "This is the logic behind everyday apps",
                ],
                "vo": "Why control flow matters: programs choose paths for discounts, menus, and checks. Loops process lists without copy-paste. This is the logic behind everyday apps.",
            },
            {
                "title": "Decisions: if / elif / else",
                "bullets": [
                    "Ask a true or false question",
                    "Run one branch when the answer is true",
                    "Use elif for more cases, else for the rest",
                ],
                "vo": "Decisions use if, elif, and else. Ask a true or false question, run one branch when the answer is true, use elif for more cases, and else for the rest.",
            },
            {
                "title": "Worked example: discount",
                "bullets": [
                    "If spend is over one hundred, apply ten percent",
                    "Elif spend is over fifty, apply five percent",
                    "Else: no discount — print the final total",
                ],
                "vo": "Worked example: a discount. If spend is over one hundred, apply ten percent. Else if spend is over fifty, apply five percent. Otherwise no discount, then print the final total.",
            },
            {
                "title": "Loops: for and while",
                "bullets": [
                    "for: walk through a known collection",
                    "while: keep going until a condition changes",
                    "Avoid infinite loops — always update the condition",
                ],
                "vo": "Loops: use for to walk through a known collection, and while to keep going until a condition changes. Avoid infinite loops by always updating the condition.",
            },
            {
                "title": "Common mistakes",
                "bullets": [
                    "Using = instead of == in comparisons",
                    "Forgetting indentation under if or for",
                    "while True with no break or stop condition",
                ],
                "vo": "Common mistakes: using a single equals instead of double equals in comparisons, forgetting indentation under if or for, and while true with no break or stop condition.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Build a tiny menu or age check",
                    "Loop through a short list and print each item",
                    "Continue in the written Module 3 lesson and quiz",
                ],
                "vo": "Practice checkpoint: build a tiny menu or age check, loop through a short list and print each item, then continue in the written Module 3 lesson and quiz.",
            },
        ],
    },
    {
        "id": "10-python-functions",
        "title": "Python Module 4 — functions lesson",
        "kind": "lesson",
        "when": "python-course, module-04-functions",
        "footer": "tutorials.html · Python Module 4",
        "pathMatch": "python-beginner-workbook/module-04-functions",
        "hubAnchor": "python-functions",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Pack steps into named functions",
                    "Pass inputs with parameters",
                    "Return results you can reuse",
                ],
                "vo": "Today’s lesson goal: pack steps into named functions, pass inputs with parameters, and return results you can reuse.",
            },
            {
                "title": "What a function is",
                "bullets": [
                    "A reusable recipe with a clear name",
                    "Call it whenever you need that work done",
                    "Keeps programs shorter and easier to test",
                ],
                "vo": "A function is a reusable recipe with a clear name. Call it whenever you need that work done. It keeps programs shorter and easier to test.",
            },
            {
                "title": "Parameters and return",
                "bullets": [
                    "Parameters are inputs the function receives",
                    "return sends a value back to the caller",
                    "Prefer return over only printing when you need the result later",
                ],
                "vo": "Parameters are inputs the function receives. Return sends a value back to the caller. Prefer return over only printing when you need the result later.",
            },
            {
                "title": "Worked example: greeting",
                "bullets": [
                    "def greet(name): return a friendly string",
                    "Call greet with different names",
                    "Reuse one function instead of copying print lines",
                ],
                "vo": "Worked example: define greet with a name parameter, return a friendly string, call it with different names, and reuse one function instead of copying print lines.",
            },
            {
                "title": "Scope in plain words",
                "bullets": [
                    "Names inside a function are local by default",
                    "Pass what you need in; return what you need out",
                    "Avoid relying on hidden global variables",
                ],
                "vo": "Scope in plain words: names inside a function are local by default. Pass what you need in, return what you need out, and avoid relying on hidden global variables.",
            },
            {
                "title": "Common mistakes",
                "bullets": [
                    "Forgetting parentheses when calling",
                    "Forgetting return and wondering why you get None",
                    "Functions that try to do five unrelated jobs",
                ],
                "vo": "Common mistakes: forgetting parentheses when calling, forgetting return and wondering why you get None, and functions that try to do five unrelated jobs.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Write one function that calculates a total",
                    "Call it twice with different inputs",
                    "Continue in the written Module 4 lesson and quiz",
                ],
                "vo": "Practice checkpoint: write one function that calculates a total, call it twice with different inputs, then continue in the written Module 4 lesson and quiz.",
            },
        ],
    },
    {
        "id": "11-python-collections",
        "title": "Python Module 5 — collections lesson",
        "kind": "lesson",
        "when": "python-course, module-05-collections",
        "footer": "tutorials.html · Python Module 5",
        "pathMatch": "python-beginner-workbook/module-05-collections",
        "hubAnchor": "python-collections",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Store many values in lists",
                    "Look up data with dictionaries",
                    "Choose the right collection for the job",
                ],
                "vo": "Today’s lesson goal: store many values in lists, look up data with dictionaries, and choose the right collection for the job.",
            },
            {
                "title": "Lists: ordered collections",
                "bullets": [
                    "Keep items in order, access by index",
                    "Append, remove, and loop through items",
                    "Great for playlists, baskets, and queues",
                ],
                "vo": "Lists are ordered collections. Keep items in order, access by index, append or remove, and loop through items. Great for playlists, baskets, and queues.",
            },
            {
                "title": "Dictionaries: keys to values",
                "bullets": [
                    "Map a key to a value — like a labelled folder",
                    "Fast lookups: name to email, id to score",
                    "Keys must be unique",
                ],
                "vo": "Dictionaries map a key to a value, like a labelled folder. Use them for fast lookups such as name to email or id to score. Keys must be unique.",
            },
            {
                "title": "Worked example: contacts",
                "bullets": [
                    "A list of friend names",
                    "A dictionary of name to phone number",
                    "Loop the list and print each number from the dictionary",
                ],
                "vo": "Worked example: keep a list of friend names and a dictionary of name to phone number, then loop the list and print each number from the dictionary.",
            },
            {
                "title": "Common mistakes",
                "bullets": [
                    "Off-by-one index errors",
                    "Assuming a key exists — use get or check first",
                    "Mixing up list order with dictionary keys",
                ],
                "vo": "Common mistakes: off-by-one index errors, assuming a key exists without checking, and mixing up list order with dictionary keys.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Build a tiny shopping list or contact book",
                    "Add, print, and look up one item",
                    "Continue in the written Module 5 lesson and quiz",
                ],
                "vo": "Practice checkpoint: build a tiny shopping list or contact book, add print and look up one item, then continue in the written Module 5 lesson and quiz.",
            },
        ],
    },
    {
        "id": "12-python-oop",
        "title": "Python Module 6 — objects lesson",
        "kind": "lesson",
        "when": "python-course, module-06-oop",
        "footer": "tutorials.html · Python Module 6",
        "pathMatch": "python-beginner-workbook/module-06-oop",
        "hubAnchor": "python-oop",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Model real things with classes",
                    "Create objects with their own data",
                    "Call methods that use that data",
                ],
                "vo": "Today’s lesson goal: model real things with classes, create objects with their own data, and call methods that use that data.",
            },
            {
                "title": "Class vs object",
                "bullets": [
                    "A class is the blueprint",
                    "An object is one built example",
                    "Many objects can share the same class",
                ],
                "vo": "A class is the blueprint. An object is one built example. Many objects can share the same class.",
            },
            {
                "title": "Attributes and methods",
                "bullets": [
                    "Attributes store data on the object",
                    "Methods are functions tied to the object",
                    "self means this particular object",
                ],
                "vo": "Attributes store data on the object. Methods are functions tied to the object. Self means this particular object.",
            },
            {
                "title": "Worked example: Task",
                "bullets": [
                    "class Task with title and done flag",
                    "mark_done method flips the flag",
                    "Create two tasks and mark one complete",
                ],
                "vo": "Worked example: a Task class with a title and done flag, a mark done method that flips the flag, then create two tasks and mark one complete.",
            },
            {
                "title": "Common mistakes",
                "bullets": [
                    "Forgetting self in method definitions",
                    "Calling the class instead of an instance method correctly",
                    "Putting all logic in one giant class",
                ],
                "vo": "Common mistakes: forgetting self in method definitions, calling methods incorrectly, and putting all logic in one giant class.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Create a simple class for a book or student",
                    "Add one method and call it",
                    "Continue in the written Module 6 lesson and quiz",
                ],
                "vo": "Practice checkpoint: create a simple class for a book or student, add one method and call it, then continue in the written Module 6 lesson and quiz.",
            },
        ],
    },
    {
        "id": "13-python-task-tracker",
        "title": "Python Module 7 — Task Tracker project lesson",
        "kind": "lesson",
        "when": "python-course, module-07-task-tracker",
        "footer": "tutorials.html · Python Module 7",
        "pathMatch": "python-beginner-workbook/module-07-task-tracker",
        "hubAnchor": "python-task-tracker",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Build a small Task Tracker end to end",
                    "Combine variables, decisions, loops, and functions",
                    "Ship something you can show on a portfolio",
                ],
                "vo": "Today’s lesson goal: build a small Task Tracker end to end, combine variables decisions loops and functions, and ship something you can show on a portfolio.",
            },
            {
                "title": "Design before you code",
                "bullets": [
                    "List features: add, list, complete, quit",
                    "Decide how tasks are stored",
                    "Sketch the menu loop on paper first",
                ],
                "vo": "Design before you code. List features like add, list, complete, and quit. Decide how tasks are stored, and sketch the menu loop on paper first.",
            },
            {
                "title": "Core loop pattern",
                "bullets": [
                    "Show a menu",
                    "Read the user’s choice",
                    "Run the matching action, then show the menu again",
                ],
                "vo": "Use a core loop pattern: show a menu, read the user’s choice, run the matching action, then show the menu again.",
            },
            {
                "title": "Make it robust",
                "bullets": [
                    "Handle empty input and bad menu choices",
                    "Confirm before deleting if you add delete",
                    "Keep messages clear for beginners testing your app",
                ],
                "vo": "Make it robust: handle empty input and bad menu choices, confirm before deleting if you add delete, and keep messages clear for beginners testing your app.",
            },
            {
                "title": "Common mistakes",
                "bullets": [
                    "Building every feature before the menu works",
                    "No way to quit the loop",
                    "Mixing storage format so list and complete disagree",
                ],
                "vo": "Common mistakes: building every feature before the menu works, no way to quit the loop, and mixing storage format so list and complete disagree.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Get add and list working first",
                    "Then add complete and quit",
                    "Follow the written Module 7 project and acceptance checks",
                ],
                "vo": "Practice checkpoint: get add and list working first, then add complete and quit, and follow the written Module 7 project and acceptance checks.",
            },
        ],
    },
    {
        "id": "14-csharp-control-flow",
        "title": "C# Module 3 — decisions & loops lesson",
        "kind": "lesson",
        "when": "csharp-course, module-03-control-flow",
        "footer": "tutorials.html · C# Module 3",
        "pathMatch": "csharp-beginner-workbook/module-03-control-flow",
        "hubAnchor": "csharp-control-flow",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Use if, else if, and else in C#",
                    "Compare values safely",
                    "Repeat work with for and while",
                ],
                "vo": "Today’s lesson goal: use if, else if, and else in C sharp, compare values safely, and repeat work with for and while.",
            },
            {
                "title": "Decisions in C#",
                "bullets": [
                    "Conditions go in parentheses",
                    "Blocks use curly braces",
                    "else if chains handle multiple cases",
                ],
                "vo": "Decisions in C sharp: conditions go in parentheses, blocks use curly braces, and else if chains handle multiple cases.",
            },
            {
                "title": "Worked example: ticket price",
                "bullets": [
                    "Child, adult, or senior based on age",
                    "Print the matching price",
                    "Else: ask for a valid age",
                ],
                "vo": "Worked example: ticket price. Choose child, adult, or senior based on age, print the matching price, and otherwise ask for a valid age.",
            },
            {
                "title": "Loops in C#",
                "bullets": [
                    "for when you know the count",
                    "while when you wait for a condition",
                    "foreach when you walk a collection",
                ],
                "vo": "Loops in C sharp: for when you know the count, while when you wait for a condition, and foreach when you walk a collection.",
            },
            {
                "title": "Common mistakes",
                "bullets": [
                    "Using = instead of ==",
                    "Missing braces so only one line is conditional",
                    "Off-by-one errors in for loops",
                ],
                "vo": "Common mistakes: using a single equals instead of double equals, missing braces so only one line is conditional, and off-by-one errors in for loops.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Write a small menu with three options",
                    "Loop until the user quits",
                    "Continue in the written Module 3 lesson and quiz",
                ],
                "vo": "Practice checkpoint: write a small menu with three options, loop until the user quits, then continue in the written Module 3 lesson and quiz.",
            },
        ],
    },
    {
        "id": "15-csharp-methods",
        "title": "C# Module 4 — methods lesson",
        "kind": "lesson",
        "when": "csharp-course, module-04-methods",
        "footer": "tutorials.html · C# Module 4",
        "pathMatch": "csharp-beginner-workbook/module-04-methods",
        "hubAnchor": "csharp-methods",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Write methods that do one clear job",
                    "Pass arguments and return values",
                    "Keep Main short by calling helpers",
                ],
                "vo": "Today’s lesson goal: write methods that do one clear job, pass arguments and return values, and keep Main short by calling helpers.",
            },
            {
                "title": "Methods are named actions",
                "bullets": [
                    "Declare return type, name, and parameters",
                    "void means it returns nothing",
                    "Call methods to reuse logic",
                ],
                "vo": "Methods are named actions. Declare return type, name, and parameters. Void means it returns nothing. Call methods to reuse logic.",
            },
            {
                "title": "Worked example: total",
                "bullets": [
                    "decimal Total(decimal price, int qty)",
                    "Return price times quantity",
                    "Print the result from Main",
                ],
                "vo": "Worked example: a Total method that takes price and quantity, returns price times quantity, then print the result from Main.",
            },
            {
                "title": "Common mistakes",
                "bullets": [
                    "Wrong return type for the value you send back",
                    "Forgetting return in non-void methods",
                    "Huge methods that mix input, math, and printing",
                ],
                "vo": "Common mistakes: wrong return type for the value you send back, forgetting return in non-void methods, and huge methods that mix input, math, and printing.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Extract one repeated calculation into a method",
                    "Call it twice from Main",
                    "Continue in the written Module 4 lesson and quiz",
                ],
                "vo": "Practice checkpoint: extract one repeated calculation into a method, call it twice from Main, then continue in the written Module 4 lesson and quiz.",
            },
        ],
    },
    {
        "id": "16-csharp-collections",
        "title": "C# Module 5 — collections lesson",
        "kind": "lesson",
        "when": "csharp-course, module-05-collections",
        "footer": "tutorials.html · C# Module 5",
        "pathMatch": "csharp-beginner-workbook/module-05-collections",
        "hubAnchor": "csharp-collections",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Use lists for ordered items",
                    "Use dictionaries for key lookups",
                    "Loop collections with foreach",
                ],
                "vo": "Today’s lesson goal: use lists for ordered items, use dictionaries for key lookups, and loop collections with foreach.",
            },
            {
                "title": "List and Dictionary",
                "bullets": [
                    "List stores items in sequence",
                    "Dictionary maps keys to values",
                    "Pick the structure that matches the problem",
                ],
                "vo": "List stores items in sequence. Dictionary maps keys to values. Pick the structure that matches the problem.",
            },
            {
                "title": "Worked example: scores",
                "bullets": [
                    "List of player names",
                    "Dictionary of name to score",
                    "foreach name, print the score",
                ],
                "vo": "Worked example: a list of player names and a dictionary of name to score, then foreach name print the score.",
            },
            {
                "title": "Common mistakes",
                "bullets": [
                    "Using arrays when a List is easier to grow",
                    "KeyNotFound when a key is missing",
                    "Mutating a collection while foreach runs",
                ],
                "vo": "Common mistakes: using arrays when a List is easier to grow, KeyNotFound when a key is missing, and mutating a collection while foreach runs.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Store three items and print them",
                    "Look up one value by key",
                    "Continue in the written Module 5 lesson and quiz",
                ],
                "vo": "Practice checkpoint: store three items and print them, look up one value by key, then continue in the written Module 5 lesson and quiz.",
            },
        ],
    },
    {
        "id": "17-csharp-oop",
        "title": "C# Module 6 — objects lesson",
        "kind": "lesson",
        "when": "csharp-course, module-06-oop-intro",
        "footer": "tutorials.html · C# Module 6",
        "pathMatch": "csharp-beginner-workbook/module-06-oop-intro",
        "hubAnchor": "csharp-oop",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Create a simple class in C#",
                    "Add properties and a method",
                    "Construct objects and use them",
                ],
                "vo": "Today’s lesson goal: create a simple class in C sharp, add properties and a method, and construct objects and use them.",
            },
            {
                "title": "Classes and objects",
                "bullets": [
                    "Class defines fields or properties",
                    "new creates an instance",
                    "Methods act on that instance’s data",
                ],
                "vo": "A class defines fields or properties. New creates an instance. Methods act on that instance’s data.",
            },
            {
                "title": "Worked example: Book",
                "bullets": [
                    "Title and IsRead properties",
                    "MarkRead method",
                    "Create two books and mark one read",
                ],
                "vo": "Worked example: a Book with Title and IsRead properties, a MarkRead method, then create two books and mark one read.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Model one real-world thing as a class",
                    "Add one behaviour method",
                    "Continue in the written Module 6 lesson and quiz",
                ],
                "vo": "Practice checkpoint: model one real-world thing as a class, add one behaviour method, then continue in the written Module 6 lesson and quiz.",
            },
        ],
    },
    {
        "id": "18-csharp-task-tracker",
        "title": "C# Module 7 — Task Tracker project lesson",
        "kind": "lesson",
        "when": "csharp-course, module-07-task-tracker",
        "footer": "tutorials.html · C# Module 7",
        "pathMatch": "csharp-beginner-workbook/module-07-task-tracker",
        "hubAnchor": "csharp-task-tracker",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Assemble a console Task Tracker",
                    "Use methods and a list of tasks",
                    "Deliver a portfolio-ready mini app",
                ],
                "vo": "Today’s lesson goal: assemble a console Task Tracker, use methods and a list of tasks, and deliver a portfolio-ready mini app.",
            },
            {
                "title": "Build in thin slices",
                "bullets": [
                    "Menu loop first",
                    "Add and list next",
                    "Complete and quit last",
                ],
                "vo": "Build in thin slices: menu loop first, add and list next, complete and quit last.",
            },
            {
                "title": "Robust behaviour",
                "bullets": [
                    "Validate menu choices",
                    "Ignore empty task titles",
                    "Show friendly messages for bad input",
                ],
                "vo": "Robust behaviour: validate menu choices, ignore empty task titles, and show friendly messages for bad input.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Ship a working add and list flow today",
                    "Then complete the written project checks",
                    "Save a short README of how to run it",
                ],
                "vo": "Practice checkpoint: ship a working add and list flow today, then complete the written project checks, and save a short README of how to run it.",
            },
        ],
    },
    {
        "id": "19-ai-prompt-patterns",
        "title": "AI Module 3 — prompt patterns lesson",
        "kind": "lesson",
        "when": "ai-course, 03-prompt-patterns",
        "footer": "tutorials.html · AI Beginner Module 3",
        "pathMatch": "languages/ai/beginner/modules/03-prompt-patterns",
        "hubAnchor": "ai-prompt-patterns",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Reuse proven prompt patterns",
                    "Extract structured fields reliably",
                    "Add a review pass that does not invent facts",
                ],
                "vo": "Today’s lesson goal: reuse proven prompt patterns, extract structured fields reliably, and add a review pass that does not invent facts.",
            },
            {
                "title": "Pattern: checklist",
                "bullets": [
                    "List required fields explicitly",
                    "Say what to do when data is missing",
                    "Reject guesses that are not in the source",
                ],
                "vo": "Checklist pattern: list required fields explicitly, say what to do when data is missing, and reject guesses that are not in the source.",
            },
            {
                "title": "Pattern: decompose then verify",
                "bullets": [
                    "Break the job into clear steps",
                    "Keep drafting separate from checking",
                    "Verify structure before you trust content",
                ],
                "vo": "Decompose then verify: break the job into clear steps, keep drafting separate from checking, and verify structure before you trust content.",
            },
            {
                "title": "Worked example: email extract",
                "bullets": [
                    "Goal: name, account, issue, urgency as JSON",
                    "Constraint: only use the email text",
                    "Repair pass: fix invalid JSON without new facts",
                ],
                "vo": "Worked example: extract name, account, issue, and urgency as JSON from an email. Only use the email text. A repair pass fixes invalid JSON without adding new facts.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Apply two patterns to the same task",
                    "Compare which fails less often",
                    "Continue in the written Module 3 lesson",
                ],
                "vo": "Practice checkpoint: apply two patterns to the same task, compare which fails less often, then continue in the written Module 3 lesson.",
            },
        ],
    },
    {
        "id": "20-ai-evaluation",
        "title": "AI Module 4 — evaluation lesson",
        "kind": "lesson",
        "when": "ai-course, 04-evaluation-and-iteration",
        "footer": "tutorials.html · AI Beginner Module 4",
        "pathMatch": "languages/ai/beginner/modules/04-evaluation-and-iteration",
        "hubAnchor": "ai-evaluation",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Build a small evaluation set",
                    "Score outputs the same way each time",
                    "Iterate with evidence, not vibes",
                ],
                "vo": "Today’s lesson goal: build a small evaluation set, score outputs the same way each time, and iterate with evidence, not vibes.",
            },
            {
                "title": "What good eval looks like",
                "bullets": [
                    "Ten or more cases: good, bad, ambiguous",
                    "Fixed rubric: format, accuracy, safety",
                    "Rerun the same set after each prompt change",
                ],
                "vo": "Good evaluation uses ten or more cases covering good, bad, and ambiguous inputs, a fixed rubric for format accuracy and safety, and reruns the same set after each prompt change.",
            },
            {
                "title": "Worked example",
                "bullets": [
                    "Case: empty input should refuse politely",
                    "Case: clear ticket should extract fields",
                    "Case: conflicting dates should ask, not invent",
                ],
                "vo": "Worked example cases: empty input should refuse politely, a clear ticket should extract fields, and conflicting dates should ask, not invent.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Write five eval cases for your prompt",
                    "Score a before and after change",
                    "Continue in the written Module 4 lesson",
                ],
                "vo": "Practice checkpoint: write five eval cases for your prompt, score a before and after change, then continue in the written Module 4 lesson.",
            },
        ],
    },
    {
        "id": "21-ai-safety",
        "title": "AI Module 5 — safety basics lesson",
        "kind": "lesson",
        "when": "ai-course, 05-safety-and-policy-basics",
        "footer": "tutorials.html · AI Beginner Module 5",
        "pathMatch": "languages/ai/beginner/modules/05-safety-and-policy-basics",
        "hubAnchor": "ai-safety",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Spot risky prompts and outputs",
                    "Add clear refusal and escalation rules",
                    "Keep user data out of places it should not go",
                ],
                "vo": "Today’s lesson goal: spot risky prompts and outputs, add clear refusal and escalation rules, and keep user data out of places it should not go.",
            },
            {
                "title": "Practical safety habits",
                "bullets": [
                    "Do not paste secrets into prompts",
                    "Refuse harmful or disallowed requests",
                    "Document what the system must never do",
                ],
                "vo": "Practical safety habits: do not paste secrets into prompts, refuse harmful or disallowed requests, and document what the system must never do.",
            },
            {
                "title": "Worked example: support bot",
                "bullets": [
                    "May summarise tickets from provided text",
                    "Must not invent refunds or legal advice",
                    "Must escalate threats to a human",
                ],
                "vo": "Worked example: a support bot may summarise tickets from provided text, must not invent refunds or legal advice, and must escalate threats to a human.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Write a short safety checklist for your use case",
                    "Add two refusal test prompts",
                    "Continue in the written Module 5 lesson",
                ],
                "vo": "Practice checkpoint: write a short safety checklist for your use case, add two refusal test prompts, then continue in the written Module 5 lesson.",
            },
        ],
    },
    {
        "id": "22-ai-workflows",
        "title": "AI Module 6 — workflows lesson",
        "kind": "lesson",
        "when": "ai-course, 06-workflows-and-automation",
        "footer": "tutorials.html · AI Beginner Module 6",
        "pathMatch": "languages/ai/beginner/modules/06-workflows-and-automation",
        "hubAnchor": "ai-workflows",
        "slides": [
            {
                "title": "Today’s lesson goal",
                "bullets": [
                    "Chain steps into a simple workflow",
                    "Keep humans in the loop where it matters",
                    "Log decisions so you can improve later",
                ],
                "vo": "Today’s lesson goal: chain steps into a simple workflow, keep humans in the loop where it matters, and log decisions so you can improve later.",
            },
            {
                "title": "Workflow thinking",
                "bullets": [
                    "Input → transform → check → output",
                    "Each step has a clear owner: model or human",
                    "Failures should stop or escalate, not silently invent",
                ],
                "vo": "Workflow thinking: input, transform, check, output. Each step has a clear owner, model or human. Failures should stop or escalate, not silently invent.",
            },
            {
                "title": "Worked example",
                "bullets": [
                    "Draft a summary",
                    "Validate required fields",
                    "Human approves before send",
                ],
                "vo": "Worked example: draft a summary, validate required fields, then a human approves before send.",
            },
            {
                "title": "Practice checkpoint",
                "bullets": [
                    "Draw a three-step workflow for a real task",
                    "Mark which steps need a human",
                    "Continue in the written Module 6 lesson",
                ],
                "vo": "Practice checkpoint: draw a three-step workflow for a real task, mark which steps need a human, then continue in the written Module 6 lesson.",
            },
        ],
    },
    {
        "id": "23-intermediate-modules-guide",
        "title": "How to study intermediate modules",
        "kind": "setup",
        "when": "advanced courses, intermediate modules",
        "footer": "tutorials.html · Intermediate tracks",
        "pathMatch": "/intermediate/modules/",
        "hubAnchor": "intermediate-guide",
        "slides": [
            {
                "title": "How these modules work",
                "bullets": [
                    "Each module builds one practical skill",
                    "Read the lesson, try the examples, then the quiz",
                    "Keep notes of decisions and tradeoffs",
                ],
                "vo": "How these intermediate modules work: each one builds one practical skill. Read the lesson, try the examples, then take the quiz, and keep notes of decisions and tradeoffs.",
            },
            {
                "title": "Study rhythm",
                "bullets": [
                    "Skim goals first",
                    "Type along with worked examples",
                    "Only then attempt Core and Better exercises",
                ],
                "vo": "Use a steady study rhythm: skim goals first, type along with worked examples, and only then attempt Core and Better exercises.",
            },
            {
                "title": "When you get stuck",
                "bullets": [
                    "Re-read the common mistakes section",
                    "Simplify the input and retry",
                    "Open Help or return to the previous module",
                ],
                "vo": "When you get stuck, re-read the common mistakes section, simplify the input and retry, or open Help and return to the previous module if needed.",
            },
            {
                "title": "Next step",
                "bullets": [
                    "Open the written lesson for this module",
                    "Mark progress as you complete quizzes",
                    "Move on when Core exercises pass your own checks",
                ],
                "vo": "Next step: open the written lesson for this module, mark progress as you complete quizzes, and move on when Core exercises pass your own checks.",
            },
        ],
    },
    {
        "id": "24-advanced-modules-guide",
        "title": "How to study advanced modules",
        "kind": "setup",
        "when": "advanced courses, advanced modules",
        "footer": "tutorials.html · Advanced tracks",
        "pathMatch": "/advanced/modules/",
        "hubAnchor": "advanced-guide",
        "slides": [
            {
                "title": "Advanced module expectations",
                "bullets": [
                    "Assume beginner fundamentals are solid",
                    "Focus on design, tradeoffs, and reliability",
                    "Treat each module like a professional brief",
                ],
                "vo": "Advanced module expectations: assume beginner fundamentals are solid, focus on design tradeoffs and reliability, and treat each module like a professional brief.",
            },
            {
                "title": "How to learn effectively",
                "bullets": [
                    "Restate the problem in your own words",
                    "Compare two approaches before coding",
                    "Write down failure modes you must avoid",
                ],
                "vo": "How to learn effectively: restate the problem in your own words, compare two approaches before coding, and write down failure modes you must avoid.",
            },
            {
                "title": "Evidence of progress",
                "bullets": [
                    "Complete the quiz to check understanding",
                    "Keep a short change log of what you tried",
                    "Link your notes to the module acceptance criteria",
                ],
                "vo": "Evidence of progress: complete the quiz to check understanding, keep a short change log of what you tried, and link your notes to the module acceptance criteria.",
            },
            {
                "title": "Next step",
                "bullets": [
                    "Open this module’s written lesson now",
                    "Work Core exercises before Beast Mode",
                    "Ask for help early on architecture questions",
                ],
                "vo": "Next step: open this module’s written lesson now, work Core exercises before Beast Mode, and ask for help early on architecture questions.",
            },
        ],
    },
]

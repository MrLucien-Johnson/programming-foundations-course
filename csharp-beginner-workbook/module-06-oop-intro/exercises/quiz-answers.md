# Module 6 Quiz Answers

## Question 1: What is the difference between a class and an object?
**Answer: B** - A class is a blueprint, an object is an instance created from that blueprint

**Explanation:** 
- **Class** = The blueprint or template (like a recipe or design)
- **Object** = A specific instance created from that class (like an actual item made from the blueprint)

**Example:**
```csharp
// Class = blueprint
class TaskItem
{
    public string Title { get; set; }
}

// Objects = specific instances
TaskItem task1 = new TaskItem();  // Object 1
TaskItem task2 = new TaskItem();  // Object 2
```

---

## Question 2: What is a constructor?
**Answer: B** - A special method that creates and initializes an object

**Explanation:** A constructor is a special method that runs when you create an object. It has the same name as the class and is used to set up the object with initial values.

**Example:**
```csharp
class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    
    // Constructor - creates and initializes the object
    public Product(string name, double price)
    {
        Name = name;
        Price = price;
    }
}

// Using the constructor
Product apple = new Product("Apple", 0.99);  // Constructor runs here
```

---

## Question 3: What is a property?
**Answer: B** - A characteristic that describes an object

**Explanation:** A property is a characteristic of an object. It stores information about the object (like a car's color or a task's title).

**Example:**
```csharp
class TaskItem
{
    public string Title { get; set; }      // Property - describes the task
    public bool IsCompleted { get; set; }  // Property - describes completion status
}

TaskItem task = new TaskItem();
task.Title = "Buy groceries";  // Setting the property
Console.WriteLine(task.Title);  // Getting the property
```

---

## Question 4: What does `new` do when creating an object?
**Answer: B** - Creates a new instance of a class

**Explanation:** The `new` keyword tells C# to create a new object (instance) from a class. It allocates memory and calls the constructor.

**Example:**
```csharp
TaskItem task = new TaskItem();
//        ↑
//     new keyword creates a new TaskItem object
```

---

## Question 5: Why do we use classes instead of just variables?
**Answer: B** - Classes organize related data and behavior together, making code easier to understand and maintain

**Explanation:** Classes let you:
- Group related data together (properties)
- Group related actions together (methods)
- Create reusable templates
- Model real-world things naturally
- Make code easier to understand and maintain

**Example:**
```csharp
// Without classes - scattered variables
string task1Title = "Buy groceries";
bool task1Complete = false;
string task2Title = "Finish report";
bool task2Complete = true;

// With classes - organized and reusable
class TaskItem
{
    public string Title { get; set; }
    public bool IsCompleted { get; set; }
}

TaskItem task1 = new TaskItem();
task1.Title = "Buy groceries";
task1.IsCompleted = false;
```

---

## True or False: A class can have multiple constructors.
**Answer: True**

**Explanation:** A class can have multiple constructors with different parameters. This is called "constructor overloading" and allows flexibility in how objects are created.

**Example:**
```csharp
class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    
    // Constructor 1 - requires name and price
    public Product(string name, double price)
    {
        Name = name;
        Price = price;
    }
    
    // Constructor 2 - only requires name (price defaults to 0)
    public Product(string name)
    {
        Name = name;
        Price = 0;
    }
}

Product p1 = new Product("Apple", 0.99);  // Uses first constructor
Product p2 = new Product("Banana");      // Uses second constructor
```

---

## True or False: Properties must always have both `get` and `set`.
**Answer: False**

**Explanation:** Properties can have just `get` (read-only), just `set` (write-only, rare), or both. However, most properties have both `get` and `set`.

**Example:**
```csharp
class Product
{
    public string Name { get; set; }           // Read and write
    public double Price { get; private set; }  // Read-only from outside
    public int Id { get; }                     // Read-only (computed property)
}
```

---

## True or False: Methods in a class can use the class's properties.
**Answer: True**

**Explanation:** Methods inside a class can access and use the class's properties. This is one of the main benefits of OOP - data and behavior are together.

**Example:**
```csharp
class Customer
{
    public string Name { get; set; }
    public string Email { get; set; }
    
    // Method uses the properties
    public void DisplayInfo()
    {
        Console.WriteLine($"Name: {Name}");    // Uses Name property
        Console.WriteLine($"Email: {Email}");   // Uses Email property
    }
}
```

---

## How Did You Do?

- **8/8 correct:** Excellent! You understand OOP basics. Ready for Module 7! 🎉
- **5-7/8 correct:** Good work! Review the questions you missed, especially around classes vs objects and constructors. You're on the right track! 👍
- **0-4/8 correct:** No worries! Re-read Module 6, focusing on:
  - What classes and objects are (blueprint vs instance)
  - How to define properties (`{ get; set; }`)
  - How to create constructors (same name as class)
  - How to create objects (`new ClassName()`)
  - How methods work in classes
  
  Take your time - OOP is a big concept! 💪

---

## Key Takeaways

1. **Class = Blueprint** - Defines what something has and can do
2. **Object = Instance** - A specific thing created from the class
3. **Properties = Characteristics** - Describe the object
4. **Constructors = Initialization** - Set up objects when created
5. **Methods = Actions** - Things objects can do
6. **OOP organizes code** - Groups related data and behavior together

**Remember:** Every expert was once a beginner. OOP is used everywhere in professional software. Keep practicing! 🚀


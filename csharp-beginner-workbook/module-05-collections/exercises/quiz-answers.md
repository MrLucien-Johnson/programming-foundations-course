# Module 5 Quiz Answers

## Question 1: What is the difference between an array and a List?
**Answer: B** - Arrays have fixed size, Lists can grow and shrink

**Explanation:** 
- **Arrays** are created with a fixed size and cannot change. Once you create an array with 5 items, it always has 5 slots.
- **Lists** can grow and shrink dynamically. You can add items, remove items, and the list adjusts automatically.

**Example:**
```csharp
// Array - fixed size
string[] days = { "Mon", "Tue", "Wed" };  // Always 3 items

// List - can grow/shrink
List<string> tasks = new List<string>();
tasks.Add("Task 1");  // Now has 1 item
tasks.Add("Task 2");  // Now has 2 items
tasks.Remove("Task 1");  // Now has 1 item again
```

---

## Question 2: How do you add an item to a List?
**Answer: B** - `list.Add("item")`

**Explanation:** The `Add()` method adds an item to the end of a list.

**Example:**
```csharp
List<string> shoppingList = new List<string>();
shoppingList.Add("Milk");
shoppingList.Add("Bread");
```

---

## Question 3: What does `foreach` do?
**Answer: B** - Loops through each item in a collection

**Explanation:** `foreach` automatically goes through each item in a collection, one at a time. You don't need to track the index.

**Example:**
```csharp
List<string> tasks = new List<string>();
tasks.Add("Buy groceries");
tasks.Add("Finish report");

foreach (string task in tasks)
{
    Console.WriteLine(task);  // Prints each task
}
```

---

## Question 4: How do you find the number of items in a collection?
**Answer: B** - `collection.Length` for arrays, `collection.Count` for lists

**Explanation:**
- **Arrays** use `.Length` property
- **Lists** use `.Count` property

**Example:**
```csharp
string[] array = { "A", "B", "C" };
int arrayCount = array.Length;  // 3

List<string> list = new List<string>();
list.Add("A");
list.Add("B");
int listCount = list.Count;  // 2
```

---

## Question 5: What is an index in a collection?
**Answer: B** - The position number of an item (starts at 0)

**Explanation:** An index is the position number of an item in a collection. **Important:** Indexes start at 0, not 1!

**Example:**
```csharp
string[] items = { "First", "Second", "Third" };
// Index 0 = "First"
// Index 1 = "Second"
// Index 2 = "Third"

Console.WriteLine(items[0]);  // Prints "First"
Console.WriteLine(items[1]);  // Prints "Second"
```

---

## True or False: Array indexes start at 1.
**Answer: False**

**Explanation:** Array indexes (and list indexes) start at 0, not 1. The first item is at index 0, the second item is at index 1, and so on.

**Example:**
```csharp
string[] items = { "A", "B", "C" };
// Index 0 = "A" (first item)
// Index 1 = "B" (second item)
// Index 2 = "C" (third item)
```

---

## True or False: You can add items to an array after it's created.
**Answer: False**

**Explanation:** Arrays have a fixed size. Once created, you cannot add or remove items. You can only change the values of existing items.

**Example:**
```csharp
string[] items = new string[3];  // Array with 3 slots
items[0] = "A";
items[1] = "B";
items[2] = "C";
// Cannot do: items.Add("D");  // Error! Arrays don't have Add()

// But Lists can:
List<string> list = new List<string>();
list.Add("A");
list.Add("B");
list.Add("C");
list.Add("D");  // ✅ This works!
```

---

## True or False: `foreach` works with both arrays and lists.
**Answer: True**

**Explanation:** `foreach` works with any collection type, including arrays and lists.

**Example:**
```csharp
// Works with arrays
string[] array = { "A", "B", "C" };
foreach (string item in array)
{
    Console.WriteLine(item);
}

// Works with lists
List<string> list = new List<string>();
list.Add("A");
list.Add("B");
foreach (string item in list)
{
    Console.WriteLine(item);
}
```

---

## How Did You Do?

- **8/8 correct:** Excellent! You understand collections. Ready for Module 6! 🎉
- **5-7/8 correct:** Good work! Review the questions you missed, especially around arrays vs lists and indexes. You're on the right track! 👍
- **0-4/8 correct:** No worries! Re-read Module 5, focusing on:
  - Difference between arrays (fixed) and lists (flexible)
  - How indexes work (start at 0!)
  - How to add items to lists (`Add()`)
  - How to loop through collections (`foreach`)
  - How to count items (`.Length` for arrays, `.Count` for lists)
  
  Take your time - these concepts are fundamental! 💪

---

## Key Takeaways

1. **Arrays are fixed-size** - Set size when created, can't change
2. **Lists are flexible** - Can add/remove items, size adjusts automatically
3. **Indexes start at 0** - First item is at index 0, not 1
4. **Use `foreach` for looping** - Easier and safer than `for` loops
5. **Arrays use `.Length`** - Lists use `.Count`
6. **Use lists when size can change** - Use arrays when size is fixed

**Remember:** Every expert was once a beginner. Keep practicing! 🚀


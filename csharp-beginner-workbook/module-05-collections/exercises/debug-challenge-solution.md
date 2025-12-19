# Debug Challenge Solution: Find the Errors

## The Broken Code

```csharp
List<string> names = new List<string>();
names.Add("Alice");
names.Add("Bob");
names.Add("Charlie");

for (int i = 0; i <= names.Count; i++)
{
    Console.WriteLine(names[i]);
}
```

## The Errors Found

### Error 1: Off-by-One Error in Loop Condition
```csharp
for (int i = 0; i <= names.Count; i++)  // ❌ Wrong condition
```

**Problem:** The condition uses `<=` (less than or equal to), which causes the loop to try accessing an index that doesn't exist.

**Explanation:**
- List has 3 items: "Alice" (index 0), "Bob" (index 1), "Charlie" (index 2)
- `names.Count` is 3
- Loop runs when `i <= 3`, so it tries: i=0, i=1, i=2, i=3
- When `i = 3`, it tries to access `names[3]`, but the list only has indexes 0, 1, 2
- This causes an "Index out of range" error!

**Should be:**
```csharp
for (int i = 0; i < names.Count; i++)  // ✅ Use < not <=
```

**Why:** With 3 items, valid indexes are 0, 1, 2. The loop should run while `i < 3`, which means i=0, i=1, i=2 (stops before i=3).

## The Fixed Code

```csharp
List<string> names = new List<string>();
names.Add("Alice");
names.Add("Bob");
names.Add("Charlie");

for (int i = 0; i < names.Count; i++)  // Fixed: Changed <= to <
{
    Console.WriteLine(names[i]);
}
```

## Even Better: Using Foreach

```csharp
List<string> names = new List<string>();
names.Add("Alice");
names.Add("Bob");
names.Add("Charlie");

foreach (string name in names)  // Much easier - no index to worry about!
{
    Console.WriteLine(name);
}
```

## Explanation of Common Errors

### Off-by-One Errors

**What it is:** Trying to access an index that doesn't exist (one too many or one too few)

**Why it happens:**
- Indexes start at 0, not 1
- Last valid index = Count - 1
- Using `<=` instead of `<` tries to access one index too many

**How to remember:**
- If list has `n` items, valid indexes are 0 through (n-1)
- Use `< Count` not `<= Count`
- Or better yet, use `foreach` - it handles this automatically!

### Visual Example

```
List with 3 items:
Index:  0        1         2
Value: "Alice"  "Bob"   "Charlie"
Count: 3

Valid access: names[0], names[1], names[2]  ✅
Invalid access: names[3]  ❌ (doesn't exist!)
```

## Common Error Messages You Might See

If you run the broken code, you might see:

```
System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection.
```

## Tips for Avoiding This Error

1. **Use `foreach` instead of `for`** - It handles bounds automatically
   ```csharp
   // Safe - no index to worry about
   foreach (string name in names)
   {
       Console.WriteLine(name);
   }
   ```

2. **If using `for`, always use `<` not `<=`**
   ```csharp
   // Correct
   for (int i = 0; i < names.Count; i++)
   ```

3. **Remember: Last index = Count - 1**
   ```csharp
   // To access last item:
   string lastItem = names[names.Count - 1];  // Not names[names.Count]!
   ```

4. **Check bounds before accessing**
   ```csharp
   int index = 5;
   if (index >= 0 && index < names.Count)
   {
       Console.WriteLine(names[index]);
   }
   ```

## Practice

Try finding the errors in this code:

```csharp
string[] items = { "A", "B", "C" };

for (int i = 0; i <= items.Length; i++)
{
    Console.WriteLine(items[i]);
}

List<int> numbers = new List<int>();
numbers.Add(10);
numbers.Add(20);

Console.WriteLine(numbers[2]);  // Try to access index 2
```

**How many errors can you find?** (Answer: 2)


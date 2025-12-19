# Exercise 2 Solution: Login Attempt Limit

## Solution Code

```csharp
string correctPassword = "secret123";
int attempts = 0;
int maxAttempts = 3;
bool accessGranted = false;

while (attempts < maxAttempts && !accessGranted)
{
    Console.Write("Enter password: ");
    string password = Console.ReadLine();
    attempts++;
    
    if (password == correctPassword)
    {
        accessGranted = true;
        Console.WriteLine("Access granted! Welcome!");
    }
    else
    {
        int remaining = maxAttempts - attempts;
        if (remaining > 0)
        {
            Console.WriteLine($"Incorrect! Attempts remaining: {remaining}");
        }
    }
}

if (!accessGranted)
{
    Console.WriteLine("Access denied. Too many failed attempts.");
}
```

## Explanation

This solution demonstrates:
1. **While loop with multiple conditions** - Continues while attempts < max AND access not granted
2. **Counter variable** - Tracks number of attempts
3. **Boolean flag** - `accessGranted` controls whether to continue looping
4. **Early exit** - Sets flag to true when password is correct
5. **Remaining attempts** - Calculates and displays attempts left

## Key Points

- Use a counter to track attempts
- Use a boolean flag to control loop exit
- Check password and set flag if correct
- Show remaining attempts after each failure
- Check flag after loop to show final message

## Variations

### Option 1: Using break
```csharp
string correctPassword = "secret123";
int attempts = 0;
int maxAttempts = 3;

while (attempts < maxAttempts)
{
    Console.Write("Enter password: ");
    string password = Console.ReadLine();
    attempts++;
    
    if (password == correctPassword)
    {
        Console.WriteLine("Access granted! Welcome!");
        break;  // Exit loop immediately
    }
    else
    {
        int remaining = maxAttempts - attempts;
        if (remaining > 0)
        {
            Console.WriteLine($"Incorrect! Attempts remaining: {remaining}");
        }
    }
}

if (attempts >= maxAttempts)
{
    Console.WriteLine("Access denied. Too many failed attempts.");
}
```

### Option 2: Simpler version
```csharp
string correctPassword = "secret123";
int attempts = 0;

while (attempts < 3)
{
    Console.Write("Enter password: ");
    string password = Console.ReadLine();
    
    if (password == correctPassword)
    {
        Console.WriteLine("Access granted! Welcome!");
        break;
    }
    
    attempts++;
    Console.WriteLine($"Incorrect! Attempts remaining: {3 - attempts}");
}

if (attempts >= 3)
{
    Console.WriteLine("Access denied. Too many failed attempts.");
}
```

### Option 3: With input validation
```csharp
string correctPassword = "secret123";
int attempts = 0;
int maxAttempts = 3;

while (attempts < maxAttempts)
{
    Console.Write("Enter password: ");
    string password = Console.ReadLine();
    
    if (string.IsNullOrEmpty(password))
    {
        Console.WriteLine("Password cannot be empty. Try again.");
        continue;  // Skip to next iteration
    }
    
    attempts++;
    
    if (password == correctPassword)
    {
        Console.WriteLine("Access granted! Welcome!");
        break;
    }
    else
    {
        int remaining = maxAttempts - attempts;
        if (remaining > 0)
        {
            Console.WriteLine($"Incorrect! Attempts remaining: {remaining}");
        }
    }
}

if (attempts >= maxAttempts)
{
    Console.WriteLine("Access denied. Too many failed attempts.");
}
```

## Common Mistakes to Avoid

1. **Infinite loop:**
   ```csharp
   // WRONG - Never increments attempts!
   int attempts = 0;
   while (attempts < 3)
   {
       Console.Write("Enter password: ");
       // Missing: attempts++;
   }
   ```

2. **Not checking after loop:**
   ```csharp
   // WRONG - Doesn't show "Access denied" message
   while (attempts < 3)
   {
       // ... code ...
   }
   // Missing check for failed attempts
   ```

3. **Wrong condition:**
   ```csharp
   // WRONG - Allows 4 attempts instead of 3!
   while (attempts <= 3)  // Should be < 3
   {
       // ...
   }
   ```

## Real-World Application

This pattern is used in:
- Login systems (email, banking, social media)
- API authentication
- Security systems
- Rate limiting
- Retry mechanisms

## Try This

Modify the program to:
- Lock account after 3 failed attempts (show lockout message)
- Add a delay between attempts (simulate security)
- Track total failed attempts
- Allow password reset after lockout
- Log failed attempts to a file (advanced)


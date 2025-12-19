# Exercise 3 Solution: Password Validation Method

## Solution Code

```csharp
static bool IsValidPassword(string password)
{
    if (password.Length >= 8 && password.Length <= 20)
    {
        return true;
    }
    else
    {
        return false;
    }
}

Console.Write("Enter a password: ");
string password = Console.ReadLine();

if (IsValidPassword(password))
{
    Console.WriteLine("Password is valid!");
}
else
{
    Console.WriteLine("Password is invalid! Must be between 8 and 20 characters.");
}
```

## Explanation

This solution demonstrates:
1. **Method returning boolean** - Returns `true` or `false`
2. **Parameter** - Takes password string as input
3. **Validation logic** - Checks length is between 8 and 20
4. **Using return value** - Caller uses the boolean result in an if statement

## Key Points

- `static bool` - Method returns a boolean (true/false)
- Uses `password.Length` to get the string length
- Checks both minimum (>= 8) and maximum (<= 20) length
- Returns `true` if valid, `false` if invalid
- Caller uses the result to display appropriate message

## Variations

### Option 1: Simplified Return
```csharp
static bool IsValidPassword(string password)
{
    // Direct return - cleaner code
    return password.Length >= 8 && password.Length <= 20;
}
```

### Option 2: With Configurable Limits
```csharp
static bool IsValidPassword(string password, int minLength, int maxLength)
{
    return password.Length >= minLength && password.Length <= maxLength;
}

// Usage:
if (IsValidPassword(password, 8, 20))
{
    Console.WriteLine("Valid!");
}
```

### Option 3: With Detailed Feedback
```csharp
static bool IsValidPassword(string password, out string message)
{
    if (password.Length < 8)
    {
        message = "Password is too short! Must be at least 8 characters.";
        return false;
    }
    else if (password.Length > 20)
    {
        message = "Password is too long! Must be no more than 20 characters.";
        return false;
    }
    else
    {
        message = "Password is valid!";
        return true;
    }
}

// Usage:
string feedback;
if (IsValidPassword(password, out feedback))
{
    Console.WriteLine(feedback);
}
else
{
    Console.WriteLine(feedback);
}
```

### Option 4: With Additional Rules
```csharp
static bool IsValidPassword(string password)
{
    // Check length
    if (password.Length < 8 || password.Length > 20)
    {
        return false;
    }
    
    // Check if contains at least one number
    bool hasNumber = false;
    foreach (char c in password)
    {
        if (char.IsDigit(c))
        {
            hasNumber = true;
            break;
        }
    }
    
    return hasNumber;
}
```

## Common Mistakes to Avoid

1. **Wrong return type:**
   ```csharp
   // WRONG - Should return bool, not string
   static string IsValidPassword(string password)  // Error!
   {
       return "true";  // This returns a string, not a boolean
   }
   ```

2. **Not returning a value:**
   ```csharp
   // WRONG - Method says it returns bool but doesn't return in all cases
   static bool IsValidPassword(string password)
   {
       if (password.Length >= 8 && password.Length <= 20)
       {
           return true;
       }
       // Missing: return false; for the else case
   }
   ```

3. **Wrong length check:**
   ```csharp
   // WRONG - This allows passwords shorter than 8
   static bool IsValidPassword(string password)
   {
       return password.Length > 8 && password.Length < 20;  // Should be >= and <=
   }
   ```

4. **Not using the return value:**
   ```csharp
   // WRONG - Calls method but ignores the result
   IsValidPassword(password);  // Result is lost!
   // Should be:
   if (IsValidPassword(password)) { ... }
   ```

## Real-World Application

This pattern is used in:
- User registration systems
- Account creation forms
- Password reset flows
- Security compliance systems
- Authentication systems

## Try This

Modify the method to:
- Check for at least one uppercase letter
- Check for at least one lowercase letter
- Check for at least one number
- Check for at least one special character
- Return which rule failed (too short, missing number, etc.)
- Make minimum and maximum length configurable


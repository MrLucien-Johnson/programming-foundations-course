# Exercise 2 Solution: Discount Calculation Method

## Solution Code

```csharp
static double CalculateDiscount(double originalPrice, double discountPercent)
{
    double discountAmount = originalPrice * discountPercent;
    double finalPrice = originalPrice - discountAmount;
    return finalPrice;
}

Console.Write("Enter original price: $");
double price = double.Parse(Console.ReadLine());

Console.Write("Enter discount percentage (e.g., 0.20 for 20%): ");
double discountPercent = double.Parse(Console.ReadLine());

double finalPrice = CalculateDiscount(price, discountPercent);
double discountAmount = price * discountPercent;

Console.WriteLine($"\nOriginal Price: ${price:F2}");
Console.WriteLine($"Discount ({discountPercent:P0}): ${discountAmount:F2}");
Console.WriteLine($"Final Price: ${finalPrice:F2}");
```

## Explanation

This solution demonstrates:
1. **Method with parameters** - Takes original price and discount percentage
2. **Method with return value** - Returns the final price after discount
3. **Calculation logic** - Calculates discount amount, then final price
4. **Reusable** - Can be called with different values

## Key Points

- `static double` - Method returns a decimal number
- Two parameters: `originalPrice` and `discountPercent`
- Calculates discount amount first, then subtracts from original
- Returns the final price
- Caller receives the result and can use it

## Variations

### Option 1: Return Discount Amount Instead
```csharp
static double CalculateDiscountAmount(double originalPrice, double discountPercent)
{
    return originalPrice * discountPercent;
}

double discount = CalculateDiscountAmount(100.00, 0.20);
double finalPrice = 100.00 - discount;
```

### Option 2: Return Both Values (using a tuple - advanced)
```csharp
static (double discount, double finalPrice) CalculateDiscount(double originalPrice, double discountPercent)
{
    double discountAmount = originalPrice * discountPercent;
    double finalPrice = originalPrice - discountAmount;
    return (discountAmount, finalPrice);
}

var result = CalculateDiscount(100.00, 0.20);
Console.WriteLine($"Discount: ${result.discount:F2}");
Console.WriteLine($"Final: ${result.finalPrice:F2}");
```

### Option 3: With Validation
```csharp
static double CalculateDiscount(double originalPrice, double discountPercent)
{
    // Validate inputs
    if (originalPrice < 0)
    {
        Console.WriteLine("Error: Price cannot be negative!");
        return 0;
    }
    
    if (discountPercent < 0 || discountPercent > 1)
    {
        Console.WriteLine("Error: Discount must be between 0 and 1!");
        return originalPrice;
    }
    
    double discountAmount = originalPrice * discountPercent;
    double finalPrice = originalPrice - discountAmount;
    return finalPrice;
}
```

### Option 4: Simplified Calculation
```csharp
static double CalculateDiscount(double originalPrice, double discountPercent)
{
    // Calculate final price directly: price * (1 - discountPercent)
    return originalPrice * (1 - discountPercent);
}
```

## Common Mistakes to Avoid

1. **Missing return type:**
   ```csharp
   // WRONG - Missing return type
   static CalculateDiscount(double price, double discount)  // Error!
   {
       return price * (1 - discount);
   }
   ```

2. **Missing parameter types:**
   ```csharp
   // WRONG - Missing types for parameters
   static double CalculateDiscount(price, discount)  // Error!
   {
       return price * (1 - discount);
   }
   ```

3. **Not returning a value:**
   ```csharp
   // WRONG - Method says it returns double but doesn't return anything
   static double CalculateDiscount(double price, double discount)
   {
       double result = price * (1 - discount);
       // Missing: return result;
   }
   ```

4. **Wrong calculation:**
   ```csharp
   // WRONG - This adds discount instead of subtracting
   static double CalculateDiscount(double price, double discount)
   {
       return price + (price * discount);  // Should be subtraction!
   }
   ```

## Real-World Application

This pattern is used in:
- E-commerce shopping carts
- Point-of-sale systems
- Promotional campaigns
- Membership discount programs
- Coupon code systems

## Try This

Modify the method to:
- Validate that discount is between 0 and 1 (0% to 100%)
- Handle maximum discount limits
- Calculate savings amount separately
- Support multiple discount types (percentage, fixed amount)
- Add tiered discounts (if price > X, apply Y%)


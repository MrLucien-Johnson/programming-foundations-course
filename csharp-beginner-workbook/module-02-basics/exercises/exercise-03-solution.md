# Exercise 3 Solution: Weekly Pay Estimator

## Solution Code

```csharp
Console.Write("Enter hours worked this week: ");
string hoursText = Console.ReadLine();
double hours = double.Parse(hoursText);

Console.Write("Enter your hourly rate: $");
string rateText = Console.ReadLine();
double rate = double.Parse(rateText);

double weeklyPay = hours * rate;

Console.WriteLine($"Hours Worked: {hours}");
Console.WriteLine($"Hourly Rate: ${rate:F2}");
Console.WriteLine($"Weekly Pay: ${weeklyPay:F2}");
```

## Explanation

This solution demonstrates:
1. **Getting decimal input** - Uses `double` for both hours and rate (supports decimals like 37.5 hours or $15.50/hour)
2. **Simple calculation** - Weekly pay = hours × rate
3. **Clear formatting** - Shows inputs and result with currency formatting

## Key Points

- `double` is used because hours can be fractional (37.5, 40.0, etc.)
- `double` is also used for rate because rates can be decimals ($15.50, $20.00, etc.)
- Calculation is straightforward: `pay = hours × rate`
- Currency formatting (`F2`) ensures professional display

## Example Run

```
Enter hours worked this week: 40
Enter your hourly rate: $15.50
Hours Worked: 40
Hourly Rate: $15.50
Weekly Pay: $620.00
```

## Variations

### Option 1: More Detailed Output
```csharp
Console.Write("Enter hours worked this week: ");
double hours = double.Parse(Console.ReadLine());

Console.Write("Enter your hourly rate: $");
double rate = double.Parse(Console.ReadLine());

double weeklyPay = hours * rate;
double monthlyPay = weeklyPay * 4;
double annualPay = weeklyPay * 52;

Console.WriteLine("\n=== Pay Summary ===");
Console.WriteLine($"Hours Worked:     {hours}");
Console.WriteLine($"Hourly Rate:       ${rate:F2}");
Console.WriteLine($"Weekly Pay:        ${weeklyPay:F2}");
Console.WriteLine($"Monthly Estimate:  ${monthlyPay:F2}");
Console.WriteLine($"Annual Estimate:   ${annualPay:F2}");
```

### Option 2: With Overtime Calculation
```csharp
const double REGULAR_HOURS = 40.0;
const double OVERTIME_RATE = 1.5;  // Time and a half

Console.Write("Enter hours worked this week: ");
double hours = double.Parse(Console.ReadLine());

Console.Write("Enter your hourly rate: $");
double rate = double.Parse(Console.ReadLine());

double regularPay;
double overtimePay = 0;

if (hours > REGULAR_HOURS)
{
    regularPay = REGULAR_HOURS * rate;
    double overtimeHours = hours - REGULAR_HOURS;
    overtimePay = overtimeHours * rate * OVERTIME_RATE;
}
else
{
    regularPay = hours * rate;
}

double totalPay = regularPay + overtimePay;

Console.WriteLine($"Regular Pay: ${regularPay:F2}");
if (overtimePay > 0)
{
    Console.WriteLine($"Overtime Pay: ${overtimePay:F2}");
}
Console.WriteLine($"Total Pay: ${totalPay:F2}");
```

## Common Mistakes to Avoid

1. **Using int instead of double:**
   ```csharp
   // WRONG - Can't handle decimal hours or rates!
   int hours = int.Parse(Console.ReadLine());  // What if user works 37.5 hours?
   int rate = int.Parse(Console.ReadLine());   // What if rate is $15.50?
   ```

2. **Wrong calculation:**
   ```csharp
   // WRONG - This doesn't make sense!
   double weeklyPay = hours + rate;  // Adding hours and rate? No!
   ```

3. **Not formatting currency:**
   ```csharp
   // Less professional
   Console.WriteLine($"Weekly Pay: ${weeklyPay}");  // Might show $620.0
   ```

## Real-World Application

This is exactly how payroll systems work:
- Time-tracking systems record hours
- HR systems store hourly rates
- Payroll calculates: hours × rate = pay
- Used in accounting, HR, and business applications

## Try This

Modify the program to:
- Calculate monthly pay (weekly × 4)
- Calculate annual pay (weekly × 52)
- Show pay after taxes (subtract a tax percentage)
- Format as a pay stub with clear sections


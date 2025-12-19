// Example 2: Getting User Input
// This demonstrates how to get input from the user and use it

Console.Write("What's your name? ");
string name = Console.ReadLine();

Console.Write("How old are you? ");
string ageText = Console.ReadLine();
int age = int.Parse(ageText);

Console.WriteLine($"Hello, {name}! You are {age} years old.");


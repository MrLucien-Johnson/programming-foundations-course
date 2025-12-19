# Enhancement 5: Save/Load Tasks to JSON File

## 🎯 Your Task

Add the ability to save tasks to a file and load them when the program starts. This way, tasks persist between program runs.

## 📝 Learning Goals

By completing this enhancement, you'll practice:
- Working with files (reading and writing)
- Using JSON format for data storage
- Loading data when program starts
- Saving data when program exits

## 🚀 Steps

1. **Add NuGet package for JSON:**
   ```bash
   dotnet add package System.Text.Json
   ```

2. **Modify `TaskItem.cs`:**
   - Make sure properties can be serialized to JSON
   - (They should work as-is with `{ get; set; }`)

3. **Modify `TaskManager.cs`:**
   - Add `SaveToFile(string filename)` method
   - Add `LoadFromFile(string filename)` method
   - Call `LoadFromFile()` in constructor
   - Call `SaveToFile()` when tasks change

4. **Modify `Program.cs`:**
   - Save tasks before exiting
   - Load tasks when starting

## 💡 Hints

- Use `System.Text.Json.JsonSerializer` for JSON
- Use `File.WriteAllText()` to save
- Use `File.ReadAllText()` to load
- Handle file not found (first run)
- Use a simple filename like "tasks.json"

## 📋 Example Code Structure

```csharp
// In TaskManager.cs
public void SaveToFile(string filename)
{
    string json = JsonSerializer.Serialize(tasks);
    File.WriteAllText(filename, json);
}

public void LoadFromFile(string filename)
{
    if (File.Exists(filename))
    {
        string json = File.ReadAllText(filename);
        tasks = JsonSerializer.Deserialize<List<TaskItem>>(json);
    }
}
```

## ✅ Tips

- Handle the case where file doesn't exist (first run)
- Save after each change (add, complete, delete)
- Or save when exiting
- Use try-catch for file operations
- Choose a clear filename

## 🎓 Real-World Connection

Data persistence is essential in real applications. Users expect their data to be saved and available the next time they use the application. This is how all professional applications work.

## 🔍 Check Your Work

Once you've added save/load:
1. Add some tasks and exit
2. Restart the program
3. Verify tasks are still there
4. Test with empty file
5. Test with corrupted file (error handling)

**Note:** This is a more advanced feature. Don't worry if it's challenging - file I/O is a next-level skill!

**Remember:** Persistence makes your application truly useful - data survives between sessions! 🎉


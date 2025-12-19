# Enhancement 4: Colored Output

Add colors to make the output more visually appealing using ANSI color codes.

## Steps

1. **Modify `task_item.py`:**
   - Update `display_info()` to use colors
   - Use green for completed tasks
   - Use yellow or default for incomplete tasks

2. **Add color constants:**
   ```python
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RESET = '\033[0m'
   ```

## Example Output

```
1. Buy groceries - ○ Incomplete  (shown in yellow)
2. Finish report - ✓ Complete    (shown in green)
```

**Note:** Colors may not work in all terminals, but the functionality is what matters most!


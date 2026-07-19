# Go Intermediate — Module 01: DSA (Practical) Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: You need average O(1) lookup of a user record by `user_id`. Which structure fits best?
**Checks outcome 1:** Choose list vs dict vs set for a given access pattern and justify the Big-O tradeoff.

A) A list you scan from the start each time  
B) A hash map/dict keyed by `user_id`  
C) A set/hash set of unsorted display names  
D) A nested list of all fields without keys  

**Your answer:** _______________

---

### Question 2: You must enforce unique email addresses and only care whether an email already exists. Best choice?
**Checks outcome 1:** Choose list vs dict vs set for a given access pattern and justify the Big-O tradeoff.

A) A list of emails  
B) A hash map/dict mapping email → full user object (required even if unused)  
C) A set/hash set of emails  
D) A queue of emails  

**Your answer:** _______________

---

### Question 3: You need to explore a graph level-by-level (nearest neighbors first). Which approach matches?
**Checks outcome 2:** Apply stack/queue and BFS/DFS mental models to a small graph or tree-style problem.

A) Depth-first search with a stack (or recursion)  
B) Breadth-first search with a queue  
C) Binary search on a sorted array  
D) LRU eviction of the oldest key  

**Your answer:** _______________

---

### Question 4: Undo/redo history in an editor is best modeled with which structure?
**Checks outcome 2:** Apply stack/queue and BFS/DFS mental models to a small graph or tree-style problem.

A) A queue (FIFO)  
B) A stack (LIFO)  
C) A hash set  
D) A priority queue ordered by timestamp only once at insert  

**Your answer:** _______________

---

### Question 5: You have a list of 50,000 comparable IDs and need them sorted once before a report. What should you do first?
**Checks outcome 3:** Decide when the language's built-in sort/search is enough versus writing a custom approach.

A) Write a custom quicksort from scratch  
B) Use the language's built-in sort unless you have a measured reason not to  
C) Always switch to a hand-rolled linked-list sort for clarity  
D) Sort with bubble sort so Big-O stays obvious  

**Your answer:** _______________

---

### Question 6: A pure function is called repeatedly with the same arguments inside a hot loop. Which pattern helps first?
**Checks outcome 4:** Apply memoization or an LRU cache when recomputation is the bottleneck.

A) Delete the function and inline random values  
B) Memoization or an LRU cache so repeated inputs reuse results  
C) Replace the dict with a list scan  
D) Disable tests to save time  

**Your answer:** _______________

---

### Question 7: An LRU cache is full and a new key arrives. What happens to the least recently used entry?
**Checks outcome 4:** Apply memoization or an LRU cache when recomputation is the bottleneck.

A) It stays forever  
B) It is evicted to make room  
C) It becomes the most recently used without eviction  
D) All keys are wiped  

**Your answer:** _______________

---

### Question 8: You want a quick before/after timing of one helper function. Best first tool?
**Checks outcome 5:** Measure a change with a micro-benchmark and explain when profiling is the better tool.

A) A micro-benchmark / timing of that function  
B) Only a full-cluster production profiler with no local measurement  
C) Guessing from code review alone  
D) Turning off tests so numbers look better  

**Your answer:** _______________

---

### Question 9: When is profiling usually better than a micro-benchmark?
**Checks outcome 5:** Measure a change with a micro-benchmark and explain when profiling is the better tool.

A) When you already know the one-line hotspot with certainty  
B) When you need to find where a whole program spends CPU or memory  
C) When you want to skip measurements entirely  
D) When sorting a 10-element list  

**Your answer:** _______________

---

### Question 10: Looking up whether an id is in a large unsorted list of IDs is typically:
**Checks outcome 1:** Choose list vs dict vs set for a given access pattern and justify the Big-O tradeoff.

A) O(1) average  
B) O(n)  
C) O(log n) without sorting  
D) O(n²) always  

**Your answer:** _______________

---

## Check Your Answers

Once you finish, check the answers file for explanations.

## How Did You Do?

- **10/10 correct:** Excellent — you can apply this module's outcomes.
- **8-9 correct:** Strong — review the missed outcome(s).
- **0-7 correct:** Revisit the lessons for those outcomes, then retry.

---

**Good luck!** Check your answers when you are ready.

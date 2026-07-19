# C# Intermediate — Module 01: DSA (Practical) Quiz Answers

## Question 1: You need average O(1) lookup of a user record by `user_id`. Which structure fits best?
**Answer: B** — A hash map/dict keyed by `user_id`

**Outcome 1:** Choose list vs dict vs set for a given access pattern and justify the Big-O tradeoff.

**Explanation:** Hash maps/dicts give average O(1) keyed lookup. Scanning a list is O(n). Sets are for membership of values, not fielded records.

---

## Question 2: You must enforce unique email addresses and only care whether an email already exists. Best choice?
**Answer: C** — A set/hash set of emails

**Outcome 1:** Choose list vs dict vs set for a given access pattern and justify the Big-O tradeoff.

**Explanation:** A set/hash set is ideal for unique membership checks. A dict works but stores unused values; a list makes uniqueness checks O(n).

---

## Question 3: You need to explore a graph level-by-level (nearest neighbors first). Which approach matches?
**Answer: B** — Breadth-first search with a queue

**Outcome 2:** Apply stack/queue and BFS/DFS mental models to a small graph or tree-style problem.

**Explanation:** BFS uses a queue and visits nodes by distance/level. DFS goes deep first. Binary search and LRU solve different problems.

---

## Question 4: Undo/redo history in an editor is best modeled with which structure?
**Answer: B** — A stack (LIFO)

**Outcome 2:** Apply stack/queue and BFS/DFS mental models to a small graph or tree-style problem.

**Explanation:** Undo reverses the most recent action first — classic LIFO/stack behavior.

---

## Question 5: You have a list of 50,000 comparable IDs and need them sorted once before a report. What should you do first?
**Answer: B** — Use the language's built-in sort unless you have a measured reason not to

**Outcome 3:** Decide when the language's built-in sort/search is enough versus writing a custom approach.

**Explanation:** Built-in sorts are highly optimized; custom sorts need measured justification.

---

## Question 6: A pure function is called repeatedly with the same arguments inside a hot loop. Which pattern helps first?
**Answer: B** — Memoization or an LRU cache so repeated inputs reuse results

**Outcome 4:** Apply memoization or an LRU cache when recomputation is the bottleneck.

**Explanation:** Memoization/LRU caching avoids recomputing identical inputs — exactly this module's caching lesson.

---

## Question 7: An LRU cache is full and a new key arrives. What happens to the least recently used entry?
**Answer: B** — It is evicted to make room

**Outcome 4:** Apply memoization or an LRU cache when recomputation is the bottleneck.

**Explanation:** LRU evicts the least recently used entry when capacity is exceeded.

---

## Question 8: You want a quick before/after timing of one helper function. Best first tool?
**Answer: A** — A micro-benchmark / timing of that function

**Outcome 5:** Measure a change with a micro-benchmark and explain when profiling is the better tool.

**Explanation:** Micro-benchmarks answer “is this function faster?” Profiling answers “where does the whole program spend time?” Start local and measured.

---

## Question 9: When is profiling usually better than a micro-benchmark?
**Answer: B** — When you need to find where a whole program spends CPU or memory

**Outcome 5:** Measure a change with a micro-benchmark and explain when profiling is the better tool.

**Explanation:** Profilers locate hotspots across a running program. Micro-benchmarks compare a narrow slice you already suspect.

---

## Question 10: Looking up whether an id is in a large unsorted list of IDs is typically:
**Answer: B** — O(n)

**Outcome 1:** Choose list vs dict vs set for a given access pattern and justify the Big-O tradeoff.

**Explanation:** Membership in an unsorted list scans elements — O(n). A set/dict membership check is average O(1).

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.

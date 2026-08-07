# Day 66 - Task Scheduler & Reorganize String

## Problems

### 1. LeetCode 621 - Task Scheduler

**Topic:** Greedy, Heap (Priority Queue)

### Approach

Count the frequency of each task and identify the task with the highest frequency. Instead of simulating the scheduling process, use a mathematical formula based on idle slots to calculate the minimum time required. Compare this value with the total number of tasks to handle cases where idle time is unnecessary.

### What I Learned

- Applying Greedy strategies to scheduling problems
- Solving scheduling without explicit simulation
- Understanding idle slot calculation
- Optimizing solutions using mathematical observations

### Difficulty Faced

Understanding why the mathematical formula always produces the minimum execution time and when it becomes equal to the total number of tasks.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

### 2. LeetCode 767 - Reorganize String

**Topic:** Greedy, Heap (Priority Queue)

### Approach

Count the frequency of each character and store them in a Max Heap (simulated using negative frequencies). Always choose the character with the highest remaining frequency while temporarily holding back the previously used character. This guarantees that no two adjacent characters are the same whenever a valid arrangement exists.

### What I Learned

- Combining Greedy algorithms with Heaps
- Simulating a Max Heap in Python
- Managing priorities dynamically
- Preventing adjacent duplicate characters

### Difficulty Faced

Understanding why the previously used character cannot immediately be inserted back into the heap and how delaying it guarantees a valid arrangement.

### Complexity

- **Time Complexity:** O(n log k)
- **Space Complexity:** O(k)

> **k = Number of distinct characters**

---

## Overall Learning

Today's problems introduced the powerful combination of **Greedy algorithms and Priority Queues**. I learned that not every scheduling problem requires simulation—sometimes mathematical reasoning leads to a much simpler solution. I also saw how Heaps can dynamically maintain priorities while Greedy decisions ensure an optimal arrangement. These patterns are extremely valuable for interview-style scheduling and string manipulation problems.

## Status

✅ Both problems accepted on LeetCode.

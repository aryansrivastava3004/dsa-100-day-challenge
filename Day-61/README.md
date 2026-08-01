# Day 61 - Kth Largest Element in an Array & Top K Frequent Elements

## Problems

### 1. LeetCode 215 - Kth Largest Element in an Array

**Topic:** Heap (Priority Queue), Arrays

### Approach

Maintain a Min Heap of size `k`. Traverse the array and insert each element into the heap. Whenever the heap size exceeds `k`, remove the smallest element. After processing all elements, the root of the heap represents the kth largest element.

### What I Learned

- Using a Min Heap to solve Top-K problems
- Maintaining a fixed-size heap for efficiency
- Avoiding full array sorting
- Applying heap operations to optimize selection problems

### Difficulty Faced

Understanding why removing the smallest element whenever the heap exceeds size `k` guarantees that the heap always contains the `k` largest elements seen so far.

### Complexity

- **Time Complexity:** O(n log k)
- **Space Complexity:** O(k)

---

### 2. LeetCode 347 - Top K Frequent Elements

**Topic:** Heap (Priority Queue), Hash Map

### Approach

Count the frequency of every element using a hash map (`Counter`). Then use `heapq.nlargest()` to retrieve the `k` elements with the highest frequencies without sorting the entire frequency map.

### What I Learned

- Combining Hash Maps with Heaps
- Counting frequencies efficiently
- Solving Top-K frequency problems
- Using Python's built-in heap utilities

### Difficulty Faced

Understanding how `heapq.nlargest()` prioritizes elements based on their frequency rather than their numerical value.

### Complexity

- **Time Complexity:** O(n log k)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems introduced one of the most important interview patterns—the **Top-K pattern**. I learned how Heaps help process only the most relevant elements instead of sorting the entire dataset. Combining Hash Maps with Heaps also showed how multiple data structures can work together to produce efficient solutions for frequency-based problems.

## Status

✅ Both problems accepted on LeetCode.

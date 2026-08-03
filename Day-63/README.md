# Day 63 - K Closest Points to Origin & Top K Frequent Words

## Problems

### 1. LeetCode 973 - K Closest Points to Origin

**Topic:** Heap (Priority Queue), Geometry

### Approach

Calculate the squared Euclidean distance of every point from the origin and store `(distance, point)` pairs in a Min Heap. Repeatedly remove the smallest distance from the heap `k` times to obtain the closest points. Squared distance is used to avoid unnecessary square root calculations while preserving the ordering.

### What I Learned

- Using custom keys with Min Heaps
- Applying Heaps to geometric problems
- Comparing squared distances instead of actual distances
- Efficiently retrieving the closest elements

### Difficulty Faced

Understanding why squared Euclidean distance produces the same ordering as the actual Euclidean distance while avoiding extra computation.

### Complexity

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 692 - Top K Frequent Words

**Topic:** Heap (Priority Queue), Hash Map

### Approach

Count the frequency of each word using `Counter`. Store `(-frequency, word)` pairs in a heap so that words with higher frequencies have higher priority. When two words have the same frequency, the heap automatically orders them lexicographically.

### What I Learned

- Combining Hash Maps with Heaps
- Custom ordering using tuples
- Solving Top-K problems on strings
- Leveraging Python's tuple comparison for tie-breaking

### Difficulty Faced

Understanding how tuple comparison automatically resolves ties by comparing the second element (the word) when frequencies are equal.

### Complexity

- **Time Complexity:** O(n + m log m)
- **Space Complexity:** O(m)

> **m = number of unique words**

---

## Overall Learning

Today's problems demonstrated how flexible the Heap data structure is. Whether working with coordinates or text data, the same Top-K pattern can be adapted by changing the comparison criteria. I also learned that choosing the right key for heap elements is crucial for solving custom sorting and priority-based problems efficiently.

## Status

✅ Both problems accepted on LeetCode.

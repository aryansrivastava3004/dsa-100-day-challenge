# Day 64 - Kth Smallest Element in a Sorted Matrix & Find K Closest Elements

## Problems

### 1. LeetCode 378 - Kth Smallest Element in a Sorted Matrix

**Topic:** Heap (Priority Queue), Sorted Matrix

### Approach

Treat each row of the matrix as a sorted list. Insert the first element of every row into a Min Heap along with its row and column indices. Repeatedly remove the smallest element from the heap and insert the next element from the same row. After removing the smallest element `k-1` times, the next element at the top of the heap is the kth smallest element.

### What I Learned

- Merging multiple sorted rows using a Min Heap
- Tracking row and column indices efficiently
- Solving Top-K problems on sorted matrices
- Applying Heap techniques to ordered data

### Difficulty Faced

Understanding why only the first element of each row needs to be inserted initially and how the heap gradually expands as elements are removed.

### Complexity

- **Time Complexity:** O(k log n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 658 - Find K Closest Elements

**Topic:** Binary Search, Sliding Window

### Approach

Instead of searching for each closest element individually, perform Binary Search on the starting index of a window of size `k`. Compare the distances of the boundary elements to determine whether the optimal window should move left or right. Once the search completes, return the selected window.

### What I Learned

- Binary Search on answer space
- Finding the optimal window instead of individual elements
- Leveraging sorted arrays for efficient searching
- Recognizing when Binary Search outperforms Heap solutions

### Difficulty Faced

Understanding why Binary Search is performed on the window's starting index rather than on individual elements.

### Complexity

- **Time Complexity:** O(log(n-k) + k)
- **Space Complexity:** O(1)

---

## Overall Learning

Today's problems highlighted two different ways of solving Top-K style questions. The Heap approach efficiently merged sorted rows to find the kth smallest element, while the Binary Search approach located the optimal window of closest elements without comparing every value individually. These problems reinforced the importance of selecting an algorithm based on the structure of the input rather than applying the same technique everywhere.

## Status

✅ Both problems accepted on LeetCode.

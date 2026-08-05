# Day 65 - Find Median from Data Stream & Merge k Sorted Lists

## Problems

### 1. LeetCode 295 - Find Median from Data Stream

**Topic:** Heap (Priority Queue), Two Heaps

### Approach

Maintain two heaps:

- A **Max Heap** (`small`) stores the smaller half of the numbers.
- A **Min Heap** (`large`) stores the larger half.

After every insertion, rebalance the heaps so their sizes differ by at most one. The median is either the top of the Max Heap (odd number of elements) or the average of both heap tops (even number of elements).

### What I Learned

- Maintaining two heaps simultaneously
- Balancing heaps after every insertion
- Efficient median calculation from streaming data
- Applying the Two Heaps pattern

### Difficulty Faced

Understanding why balancing the heap sizes after each insertion guarantees constant-time median retrieval.

### Complexity

- **addNum():** O(log n)
- **findMedian():** O(1)
- **Space Complexity:** O(n)

---

### 2. LeetCode 23 - Merge k Sorted Lists

**Topic:** Heap (Priority Queue), Linked List

### Approach

Insert the first node of every linked list into a Min Heap. Repeatedly remove the smallest node, attach it to the merged list, and insert the next node from the same linked list. Continue until the heap becomes empty.

### What I Learned

- Merging multiple sorted linked lists efficiently
- Using a Min Heap with linked list nodes
- Processing one node from each list at a time
- Applying Heap techniques to linked data structures

### Difficulty Faced

Understanding why only the current node from each list needs to remain inside the heap instead of storing every node.

### Complexity

- **Time Complexity:** O(N log k)
- **Space Complexity:** O(k)

> **N = Total number of nodes**
>
> **k = Number of linked lists**

---

## Overall Learning

Today's problems introduced two of the most important Heap applications used in coding interviews. I learned how the **Two Heaps** pattern enables efficient median calculation from a continuous stream of numbers, while the **Heap Merge** pattern efficiently combines multiple sorted linked lists. These problems demonstrated that Priority Queues are powerful tools for handling dynamic data and merging ordered structures efficiently.

## Status

✅ Both problems accepted on LeetCode.

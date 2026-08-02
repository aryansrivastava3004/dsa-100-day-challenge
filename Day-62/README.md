# Day 62 - Kth Largest Element in a Stream & Last Stone Weight

## Problems

### 1. LeetCode 703 - Kth Largest Element in a Stream

**Topic:** Heap (Priority Queue), Data Stream

### Approach

Maintain a Min Heap of size `k`. During initialization, heapify the input array and remove the smallest elements until only the `k` largest remain. For each new value added to the stream, insert it into the heap and remove the smallest element if the heap exceeds size `k`. The root of the heap always represents the kth largest element.

### What I Learned

- Maintaining a fixed-size Min Heap
- Processing streaming data efficiently
- Updating answers dynamically
- Applying Heap operations to online algorithms

### Difficulty Faced

Understanding why storing only the `k` largest elements is sufficient and why the root of the Min Heap always represents the kth largest value.

### Complexity

- **Constructor:** O(n log k)
- **add():** O(log k)
- **Space Complexity:** O(k)

---

### 2. LeetCode 1046 - Last Stone Weight

**Topic:** Heap (Priority Queue), Simulation

### Approach

Since Python provides a Min Heap, convert all stone weights into negative values to simulate a Max Heap. Repeatedly remove the two heaviest stones, smash them together, and insert the remaining weight back into the heap if necessary. Continue until one or no stones remain.

### What I Learned

- Simulating a Max Heap using negative values
- Efficiently retrieving the largest elements
- Applying Heap operations in simulation problems
- Managing dynamic collections with Priority Queues

### Difficulty Faced

Understanding how negating values transforms Python's Min Heap into an efficient Max Heap implementation.

### Complexity

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems strengthened my understanding of Heaps by applying them to streaming data and simulation-based scenarios. I learned how maintaining only the necessary elements can significantly improve efficiency and how Priority Queues simplify problems involving repeated maximum or minimum operations.

## Status

✅ Both problems accepted on LeetCode.

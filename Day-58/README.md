# Day 58 - Binary Tree Zigzag Level Order Traversal & Populating Next Right Pointers in Each Node

## Problems

### 1. LeetCode 103 - Binary Tree Zigzag Level Order Traversal

**Topic:** Binary Tree, Breadth-First Search (BFS), Level Order Traversal

### Approach

Perform a standard level-order traversal using a queue. After processing each level, alternate the traversal direction by reversing the current level whenever required. A boolean flag keeps track of the traversal direction.

### What I Learned

- Performing zigzag traversal using BFS
- Alternating traversal direction after every level
- Using a boolean flag to simplify logic
- Reusing level-order traversal for different tree problems

### Difficulty Faced

Remembering to reverse only the current level instead of changing the traversal of the queue itself.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 116 - Populating Next Right Pointers in Each Node

**Topic:** Binary Tree, Breadth-First Search (BFS), Queue

### Approach

Use BFS to process one level at a time. While traversing a level, connect each node to the next node using the `next` pointer. The last node of every level points to `NULL`.

### What I Learned

- Connecting nodes horizontally using BFS
- Processing one level completely before moving to the next
- Maintaining references between adjacent nodes
- Applying queues to modify Binary Tree structures

### Difficulty Faced

Keeping track of the previous node while traversing each level so that the `next` pointers are assigned correctly.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems expanded my understanding of Breadth-First Search by showing how the same level-order traversal can be adapted for different objectives. Whether alternating the traversal direction or connecting nodes at the same level, these problems reinforced the flexibility of BFS and strengthened my understanding of Binary Tree traversal patterns.

## Status

✅ Both problems accepted on LeetCode.

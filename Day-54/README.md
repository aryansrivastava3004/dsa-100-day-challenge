# Day 54 - Binary Tree Right Side View & Average of Levels in Binary Tree

## Problems

### 1. LeetCode 199 - Binary Tree Right Side View

**Topic:** Binary Tree, Breadth-First Search (BFS), Level Order Traversal

### Approach

Perform a level-order traversal using a queue. For each level, process all nodes from left to right and record the value of the last node visited. Since it is the final node of that level, it represents the view from the right side of the tree.

### What I Learned

- Performing level-order traversal using BFS
- Processing one level at a time with a queue
- Identifying the rightmost node of each level
- Applying the same BFS pattern to tree-view problems

### Difficulty Faced

Understanding why the last node processed at every level corresponds to the node visible from the right side of the tree.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 637 - Average of Levels in Binary Tree

**Topic:** Binary Tree, Breadth-First Search (BFS), Queue

### Approach

Use a queue to perform level-order traversal. While processing each level, calculate the sum of node values and divide it by the number of nodes in that level to compute the average.

### What I Learned

- Calculating aggregate values during BFS
- Using queue size to separate tree levels
- Computing averages efficiently during traversal
- Reusing the same traversal strategy for different objectives

### Difficulty Faced

Remembering to determine the number of nodes in the current level before processing it, ensuring each average is calculated correctly.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems reinforced the power of Breadth-First Search in Binary Trees. By processing one level at a time, I learned how the same traversal pattern can solve completely different problems—from identifying the right-side view of a tree to calculating the average value at every level. This strengthened my understanding of level-order traversal as a fundamental tree algorithm.

## Status

✅ Both problems accepted on LeetCode.

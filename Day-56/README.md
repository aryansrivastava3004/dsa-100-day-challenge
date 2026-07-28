# Day 56 - Sum Root to Leaf Numbers & Path Sum II

## Problems

### 1. LeetCode 129 - Sum Root to Leaf Numbers

**Topic:** Binary Tree, Depth-First Search (DFS), Recursion

### Approach

Perform a DFS traversal while maintaining the number formed from the root to the current node. At each step, multiply the current number by 10 and add the current node's value. When a leaf node is reached, return the completed number. Sum the values returned from all root-to-leaf paths.

### What I Learned

- Building numbers during tree traversal
- Passing values recursively
- Identifying leaf nodes efficiently
- Applying DFS to solve path-based problems

### Difficulty Faced

Understanding how to update the current number at each recursive call and return the sum from multiple root-to-leaf paths.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 113 - Path Sum II

**Topic:** Binary Tree, Depth-First Search (DFS), Backtracking

### Approach

Use DFS to explore every root-to-leaf path while maintaining both the current path and its sum. Whenever a leaf node is reached with the required target sum, store a copy of the current path. Use backtracking by removing the last node before returning from recursion.

### What I Learned

- Combining DFS with backtracking
- Tracking root-to-leaf paths
- Copying lists before storing results
- Restoring the current path during recursion

### Difficulty Faced

Remembering to backtrack correctly by removing the last node from the current path after exploring each subtree.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems strengthened my understanding of path-based Binary Tree algorithms. I learned how recursion can carry useful information throughout a traversal, whether it's constructing numbers or tracking complete paths. Backtracking also helped me understand how to explore multiple paths without affecting previous results. These patterns are widely used in many advanced tree and graph problems.

## Status

✅ Both problems accepted on LeetCode.

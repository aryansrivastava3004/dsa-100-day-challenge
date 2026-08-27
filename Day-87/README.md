# Day 87 - Maximum Width of Binary Tree & Find Largest Value in Each Tree Row

## Problems

### 1. LeetCode 662 - Maximum Width of Binary Tree

**Topic:** Binary Trees, BFS, Level Order Traversal

### Approach

Use BFS to process the tree level by level.

Assign each node a positional index as if the tree were a complete binary tree:

- Left child → `2 × index`
- Right child → `2 × index + 1`

For every level, calculate:

`width = last_index - first_index + 1`

This accounts for the gaps created by missing nodes.

### What I Learned

- Level-order traversal using BFS
- Representing tree positions using indices
- Handling missing nodes while calculating width
- Using additional information during BFS

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 515 - Find Largest Value in Each Tree Row

**Topic:** Binary Trees, BFS, Level Order Traversal

### Approach

Use BFS to process every level separately.

For each level, keep track of the maximum node value. After processing the complete level, add that maximum value to the result.

### What I Learned

- Processing trees level by level
- Finding aggregate information from each level
- Using BFS with level boundaries
- Reusing the same traversal pattern for different problems

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems reinforced the usefulness of **Level Order Traversal**.

Both problems use BFS, but extract different information from each tree level. Maximum Width uses positional information, while Largest Value in Each Tree Row tracks the maximum value.

The biggest takeaway was that once the basic BFS pattern is understood, it can be adapted to solve many different binary tree problems.

## Status

✅ Both problems accepted on LeetCode.

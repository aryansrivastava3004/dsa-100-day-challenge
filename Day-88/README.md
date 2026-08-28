# Day 88 - Find Bottom Left Tree Value & Check Completeness of a Binary Tree

## Problems

### 1. LeetCode 513 - Find Bottom Left Tree Value

**Topic:** Binary Trees, BFS, Level Order Traversal

### Approach

Use BFS while adding the right child before the left child.

This reverses the normal left-to-right processing order. As a result, the last node processed will be the leftmost node at the deepest level.

### What I Learned

- Using BFS for binary tree problems
- Understanding how traversal order can simplify a solution
- Finding the deepest leftmost node
- Using a queue to control traversal order

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 958 - Check Completeness of a Binary Tree

**Topic:** Binary Trees, BFS, Level Order Traversal

### Approach

Use level-order traversal and add both children to the queue, including `None`.

Once a `None` node is encountered, no actual node should appear afterward in a complete binary tree.

If an actual node is found after a missing position, the tree is not complete.

### What I Learned

- Understanding the structure of a complete binary tree
- Using BFS to validate tree structure
- Using `None` nodes as structural information
- Detecting invalid positions during level-order traversal

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems reinforced the power of **BFS and traversal order** in binary tree problems.

For Find Bottom Left Tree Value, changing the order in which children are added to the queue allows the required node to naturally become the last processed node.

For Check Completeness of a Binary Tree, tracking the first missing position helps determine whether the remaining tree follows the required left-to-right structure.

The biggest takeaway was that sometimes the key to a tree problem isn't a complicated algorithm, but choosing the right **traversal order and state to maintain**.

## Status

✅ Both problems accepted on LeetCode.

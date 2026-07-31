# Day 60 - Count Complete Tree Nodes & Binary Search Tree Iterator

## Problems

### 1. LeetCode 222 - Count Complete Tree Nodes

**Topic:** Binary Tree, Complete Binary Tree, Divide & Conquer

### Approach

Instead of visiting every node, compare the height of the leftmost path and the rightmost path. If both heights are equal, the tree is a perfect binary tree, and the number of nodes can be calculated directly using the formula:

`2^(height + 1) - 1`

Otherwise, recursively count the nodes in the left and right subtrees.

### What I Learned

- Properties of Complete Binary Trees
- Identifying Perfect Binary Trees
- Optimizing recursive solutions using tree properties
- Applying Divide & Conquer to reduce time complexity

### Difficulty Faced

Understanding why equal left and right heights guarantee that the tree is perfect and how this optimization avoids traversing every node.

### Complexity

- **Time Complexity:** O(log² n)
- **Space Complexity:** O(log n)

---

### 2. LeetCode 173 - Binary Search Tree Iterator

**Topic:** Binary Search Tree, Stack, Inorder Traversal

### Approach

Simulate an inorder traversal using a stack. Initially, push all the left children onto the stack. Whenever `next()` is called, pop the top node and push all left children of its right subtree. This ensures nodes are returned in sorted order without traversing the entire tree beforehand.

### What I Learned

- Simulating inorder traversal iteratively
- Using a stack efficiently
- Lazy traversal of a BST
- Designing iterator-based data structures

### Difficulty Faced

Understanding why only the leftmost path is stored initially and how pushing the left path of the right subtree maintains sorted traversal.

### Complexity

- **Time Complexity:**
  - `next()` → O(1) amortized
  - `hasNext()` → O(1)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems introduced two efficient techniques for working with trees. I learned how the properties of a Complete Binary Tree can be used to optimize recursive solutions beyond the standard O(n) traversal. I also explored iterator design by implementing lazy inorder traversal using a stack, reinforcing the importance of choosing the right data structure for efficient tree operations.

## Status

✅ Both problems accepted on LeetCode.

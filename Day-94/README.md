# Day 94 - Trim a Binary Search Tree & Increasing Order Search Tree

## Problems

### 1. LeetCode 669 - Trim a Binary Search Tree

**Topic:** Binary Search Tree, Recursion

### Approach

Use the BST property to remove nodes outside the given range.

If the current node is smaller than `low`, everything in its left subtree is also too small, so we only need to process the right subtree.

If the current node is greater than `high`, everything in its right subtree is too large, so we only process the left subtree.

Otherwise, keep the node and recursively trim both subtrees.

### What I Learned

- Using BST properties to eliminate unnecessary branches
- Recursively modifying a binary tree
- Understanding how node values determine which subtree to search

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 897 - Increasing Order Search Tree

**Topic:** Binary Search Tree, Inorder Traversal, Recursion

### Approach

Perform an inorder traversal of the BST.

Since inorder traversal of a BST produces values in sorted order, create a new tree where every node has no left child and points to the next value using its right child.

### What I Learned

- Using inorder traversal to obtain sorted BST values
- Transforming a BST into a right-skewed tree
- Using recursion to construct a new tree structure
- Understanding the relationship between BSTs and sorted order

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems reinforced the importance of the BST property.

For trimming a BST, the ordering of values allows entire subtrees to be ignored. For the increasing order tree, the same ordering makes inorder traversal naturally produce the required sorted sequence.

The biggest takeaway was that **understanding the properties of a data structure can help us avoid unnecessary work and simplify the solution.**

## Status

✅ Both problems accepted on LeetCode.

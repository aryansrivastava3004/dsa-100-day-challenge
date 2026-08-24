# Day 84 - Recover Binary Search Tree & Convert Sorted Array to BST

## Problems

### 1. LeetCode 99 - Recover Binary Search Tree

**Topic:** Binary Search Tree, Inorder Traversal, Recursion

### Approach

A valid BST produces values in sorted order during inorder traversal.

If two nodes are swapped, the inorder traversal will contain one or two ordering violations.

Track the previous node while performing inorder traversal. Identify the two incorrect nodes and swap their values to restore the BST.

### What I Learned

- Using inorder traversal to validate BST ordering
- Detecting misplaced nodes
- Recovering a BST without changing its structure
- Using recursion with maintained state

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 108 - Convert Sorted Array to Binary Search Tree

**Topic:** Binary Search Tree, Recursion, Divide and Conquer

### Approach

Since the array is sorted, choose its middle element as the root.

The left half becomes the left subtree and the right half becomes the right subtree. Repeating this recursively produces a height-balanced BST.

### What I Learned

- Building a balanced BST from sorted data
- Choosing the middle element as the root
- Applying divide and conquer
- Understanding the relationship between sorted arrays and BSTs

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems reinforced the importance of the **BST ordering property**.

Inorder traversal allows us to detect and recover a corrupted BST, while the sorted nature of an array allows us to construct a balanced BST directly.

The biggest takeaway was seeing how the same BST property can be used both to **analyze an existing tree and construct a new one**.

## Status

✅ Both problems accepted on LeetCode.

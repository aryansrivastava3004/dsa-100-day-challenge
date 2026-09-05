# Day 96 - Second Minimum Node & Construct BST from Preorder

## Problems

### 1. LeetCode 671 - Second Minimum Node In a Binary Tree

**Topic:** Binary Trees, DFS, Sets

### Approach

Traverse the entire binary tree using DFS and store all unique node values in a set.

After traversal, sort the unique values and return the second smallest value.

If there is only one unique value, return `-1`.

### What I Learned

- Traversing a binary tree using DFS
- Using sets to store unique values
- Finding the second minimum value
- Handling cases with insufficient unique values

### Complexity

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal

**Topic:** Binary Search Tree, Recursion, Preorder Traversal

### Approach

Preorder traversal follows:

Root → Left → Right

Using the BST property, values smaller than the current root belong to the left subtree, while larger values belong to the right subtree.

A boundary is maintained for every recursive call to determine whether the next value belongs to the current subtree.

### What I Learned

- Understanding preorder traversal
- Reconstructing a BST from its preorder traversal
- Using BST ordering properties
- Using bounds with recursion
- Building a tree in a single traversal

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems focused on using the properties of binary trees and BSTs to extract information and reconstruct tree structures.

The first problem used DFS and a set to find the second minimum value, while the second used preorder traversal and BST bounds to reconstruct the tree efficiently.

The biggest takeaway was that **understanding the structure and properties of a tree can greatly simplify the solution.**

## Status

✅ Both problems accepted on LeetCode.

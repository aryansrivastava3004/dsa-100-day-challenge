# Day 85 - Construct Binary Tree from Traversals

## Problems

### 1. LeetCode 105 - Construct Binary Tree from Preorder and Inorder Traversal

**Topic:** Binary Trees, Recursion, Tree Traversal

### Approach

In preorder traversal, the first element is always the root.

Find this root in the inorder traversal. Everything before it belongs to the left subtree, while everything after it belongs to the right subtree.

Repeat the same process recursively for both subtrees.

### What I Learned

- Understanding preorder and inorder traversal
- Identifying the root from preorder
- Using inorder to separate left and right subtrees
- Reconstructing a binary tree recursively

### Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n)

---

### 2. LeetCode 106 - Construct Binary Tree from Inorder and Postorder Traversal

**Topic:** Binary Trees, Recursion, Tree Traversal

### Approach

In postorder traversal, the last element is always the root.

Find this root in the inorder traversal and split the remaining elements into the left and right subtrees.

Repeat recursively until the complete tree is constructed.

### What I Learned

- Understanding postorder and inorder traversal
- Identifying the root from postorder
- Using inorder to determine subtree boundaries
- Applying the same recursive pattern to a different traversal combination

### Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems demonstrated that tree traversals contain enough information to reconstruct a binary tree.

Preorder gives the root from the beginning, postorder gives the root from the end, and inorder tells us how to divide the tree into left and right subtrees.

The biggest takeaway was recognizing that both problems follow the same underlying recursive pattern.

## Status

✅ Both problems accepted on LeetCode.

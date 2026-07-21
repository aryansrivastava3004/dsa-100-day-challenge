# Day 51 - Insert into a Binary Search Tree & Kth Smallest Element in a BST

## Problems

### 1. LeetCode 701 - Insert into a Binary Search Tree

**Topic:** Binary Search Tree (BST), Recursion

### Approach

Traverse the Binary Search Tree recursively. Compare the value to be inserted with the current node's value and move left or right accordingly. Once a null position is reached, create a new node and attach it while preserving the BST property.

### What I Learned

- Recursive insertion in a BST
- Preserving BST ordering after insertion
- Returning updated subtrees during recursion
- Understanding how recursion reconnects modified child nodes

### Difficulty Faced

Initially, it was confusing why each recursive call returns a subtree. I learned that returning the subtree ensures the parent node correctly reconnects to the updated child after insertion.

### Complexity

- **Time Complexity:** O(h)
- **Space Complexity:** O(h)

---

### 2. LeetCode 230 - Kth Smallest Element in a BST

**Topic:** Binary Search Tree (BST), Inorder Traversal, Stack

### Approach

Perform an iterative inorder traversal using a stack. Since inorder traversal of a BST visits nodes in ascending order, decrement `k` after visiting each node. When `k` becomes zero, return the current node's value.

### What I Learned

- Iterative inorder traversal using a stack
- Why inorder traversal of a BST produces sorted values
- Finding the kth smallest element efficiently
- Using stack-based traversal instead of recursion

### Difficulty Faced

Understanding how the iterative inorder traversal works without recursion and why the kth visited node is always the kth smallest element.

### Complexity

- **Time Complexity:** O(h + k)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems deepened my understanding of Binary Search Trees. I learned how insertion maintains the BST property and how inorder traversal leverages the ordered structure of BSTs to solve problems efficiently. These concepts are fundamental for many advanced tree-based interview questions.

## Status

✅ Both problems accepted on LeetCode.

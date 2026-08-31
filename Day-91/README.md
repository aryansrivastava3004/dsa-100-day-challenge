# Day 91 - Binary Tree Inorder Traversal & Find Duplicate Subtrees

## Problems

### 1. LeetCode 94 - Binary Tree Inorder Traversal

**Topic:** Binary Trees, Recursion, Tree Traversal

### Approach

Perform an inorder traversal using recursion.

The traversal follows:

Left → Root → Right

The values are added to the result when the current node is processed.

### What I Learned

- Understanding inorder traversal
- Using recursion for tree traversal
- Processing left and right subtrees in the correct order
- Building a result list during traversal

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 652 - Find Duplicate Subtrees

**Topic:** Binary Trees, DFS, Hashing, Recursion

### Approach

Represent every subtree using a unique signature containing:

- Current node value
- Left subtree representation
- Right subtree representation

Store the frequency of each signature in a Hash Map.

When a signature appears for the second time, the corresponding subtree is added to the result.

### What I Learned

- Representing tree structures uniquely
- Using DFS to process subtrees
- Using Hash Maps to detect duplicate structures
- Combining recursion with hashing
- Comparing complex tree structures through serialization

### Complexity

- **Time Complexity:** O(n²) worst case
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems focused on understanding and representing binary tree structures.

Inorder Traversal strengthened the fundamentals of recursive tree traversal, while Duplicate Subtrees introduced a more advanced technique of creating unique representations for subtrees and using hashing to identify repeated structures.

The biggest takeaway was that **tree structure itself can be converted into useful data that allows us to compare and analyze subtrees efficiently.**

## Status

✅ Both problems accepted on LeetCode.

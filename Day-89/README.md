# Day 89 - Binary Tree Level Order Traversal II & Construct Binary Tree from Preorder and Postorder Traversal

## Problems

### 1. LeetCode 107 - Binary Tree Level Order Traversal II

**Topic:** Binary Trees, BFS, Level Order Traversal

### Approach

Perform a standard level-order traversal using BFS and store each level in the result.

Since the required output is from bottom to top, reverse the result at the end.

### What I Learned

- Using BFS for level-order traversal
- Processing a tree one level at a time
- Modifying standard traversal to produce bottom-up output
- Using a simple reversal to change traversal direction

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 889 - Construct Binary Tree from Preorder and Postorder Traversal

**Topic:** Binary Trees, Recursion, Tree Traversal

### Approach

In preorder traversal, the first element is the root.

The second element represents the root of the left subtree. Find this value in postorder to determine the size of the left subtree.

Then recursively construct the left and right subtrees.

### What I Learned

- Understanding the relationship between preorder and postorder traversal
- Reconstructing a binary tree from traversal sequences
- Finding subtree boundaries
- Applying recursion to tree construction

### Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems reinforced how traversal patterns can be adapted to solve different tree problems.

Level-order traversal can be reversed to produce bottom-up results, while preorder and postorder together can be used to reconstruct a binary tree.

The biggest takeaway was learning to identify what information each traversal provides and how to combine that information effectively.

## Status

✅ Both problems accepted on LeetCode.

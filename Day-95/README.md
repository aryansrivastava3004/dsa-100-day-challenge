# Day 95 - Range Sum of BST & Two Sum IV

## Problems

### 1. LeetCode 938 - Range Sum of BST

**Topic:** Binary Search Tree, Recursion, Tree Traversal

### Approach

Use the BST property to avoid visiting unnecessary subtrees.

If the current value is smaller than `low`, the entire left subtree is also smaller, so only the right subtree needs to be explored.

If the current value is greater than `high`, the entire right subtree is too large, so only the left subtree needs to be explored.

If the value lies within the range, include it and recursively search both subtrees.

### What I Learned

- Using BST properties for pruning
- Finding values within a specific range
- Using recursion for efficient tree traversal
- Avoiding unnecessary subtree traversal

### Complexity

- **Time Complexity:** O(n) worst case
- **Space Complexity:** O(h)

---

### 2. LeetCode 653 - Two Sum IV - Input is a BST

**Topic:** Binary Search Tree, DFS, Hashing

### Approach

Traverse the tree using DFS while maintaining a set of values already visited.

For each node, calculate the value needed to reach the target:

`needed = k - node.val`

If the required value is already present in the set, a valid pair has been found.

### What I Learned

- Applying the Two Sum technique to a binary tree
- Using a Hash Set for constant-time lookups
- Combining DFS with hashing
- Finding complementary values while traversing a tree

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems focused on combining the properties of Binary Search Trees with familiar techniques such as recursion and hashing.

Range Sum of BST showed how the ordering of a BST can help eliminate unnecessary searches, while Two Sum IV demonstrated how a Hash Set can be combined with tree traversal to efficiently find a pair of values.

The biggest takeaway was that **understanding the structure of the data can help make standard problem-solving techniques more efficient.**

## Status

✅ Both problems accepted on LeetCode.

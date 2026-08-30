# Day 90 - Subtree of Another Tree & Maximum Binary Tree

## Problems

### 1. LeetCode 572 - Subtree of Another Tree

**Topic:** Binary Trees, Recursion, Tree Comparison

### Approach

Traverse the main tree and check whether the tree rooted at each node is identical to `subRoot`.

Two recursive functions are used:

- `isSubtree()` searches for a possible matching subtree.
- `isSameTree()` checks whether two trees are structurally and numerically identical.

### What I Learned

- Comparing binary trees recursively
- Searching for a subtree within another tree
- Breaking tree problems into smaller recursive comparisons
- Checking both structure and node values

### Complexity

- **Time Complexity:** O(n × m)
- **Space Complexity:** O(h)

---

### 2. LeetCode 654 - Maximum Binary Tree

**Topic:** Binary Trees, Recursion, Divide and Conquer

### Approach

Find the maximum element in the array and make it the root.

The elements before the maximum form the left subtree, while the elements after it form the right subtree.

Repeat the same process recursively for both parts.

### What I Learned

- Constructing a binary tree recursively
- Using the maximum element to determine the root
- Dividing an array into left and right subtrees
- Applying divide and conquer to tree construction

### Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems focused on understanding how recursion can be used both to **analyze existing tree structures** and to **construct new ones**.

The biggest takeaway was recognizing that a binary tree naturally breaks a problem into smaller left and right subtree problems.

## Status

✅ Both problems accepted on LeetCode.

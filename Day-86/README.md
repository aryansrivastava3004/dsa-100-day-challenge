# Day 86 - Binary Tree Maximum Path Sum & Path Sum III

## Problems

### 1. LeetCode 124 - Binary Tree Maximum Path Sum

**Topic:** Binary Trees, DFS, Recursion, Dynamic Programming

### Approach

For every node, calculate the maximum contribution that can be passed to its parent.

A path passing through the current node can use both the left and right subtrees, so update the global maximum using:

`node + left + right`

When returning to the parent, only one branch can be used because a path cannot split into two directions.

Negative subtree contributions are ignored.

### What I Learned

- Finding maximum paths in binary trees
- Using DFS to calculate information from subtrees
- Handling negative values
- Maintaining a global maximum during recursion
- Understanding the difference between a path used for the answer and a path returned to the parent

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 437 - Path Sum III

**Topic:** Binary Trees, DFS, Prefix Sum

### Approach

Use DFS together with Prefix Sum.

For the current prefix sum:

`current_sum - previous_sum = targetSum`

Therefore, if `current_sum - targetSum` has appeared before, there are paths ending at the current node whose sum equals the target.

A Hash Map stores the frequency of prefix sums along the current root-to-node path.

### What I Learned

- Combining DFS with Prefix Sum
- Counting paths efficiently
- Using a Hash Map to store prefix-sum frequencies
- Maintaining and removing state during recursive traversal

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems showed that DFS can carry much more information than simply whether a node has been visited.

**Binary Tree Maximum Path Sum** uses information from both subtrees to determine the best path, while **Path Sum III** combines DFS with Prefix Sum to count valid paths efficiently.

The biggest takeaway was learning how to maintain useful state throughout a tree traversal and use it to solve more complex path-based problems.

## Status

✅ Both problems accepted on LeetCode.

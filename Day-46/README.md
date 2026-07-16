# Day 46 - Diameter of Binary Tree & Binary Tree Level Order Traversal

## Problems

### 1. LeetCode 543 - Diameter of Binary Tree

**Topic:** Binary Tree, Depth-First Search (DFS), Recursion

#### Approach

Recursively calculate the height of each subtree. At every node, compute the sum of the heights of its left and right subtrees, which represents the longest path passing through that node. Keep updating the maximum diameter found during the traversal.

#### What I Learned

- Calculating subtree heights recursively
- Updating a global answer during recursion
- Understanding the diameter of a binary tree
- Using `nonlocal` variables inside nested functions

#### Difficulty Faced

Understanding that the diameter is calculated using the heights of both subtrees rather than simply considering the maximum depth of the tree.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(h)

---

### 2. LeetCode 102 - Binary Tree Level Order Traversal

**Topic:** Binary Tree, Breadth-First Search (BFS), Queue

#### Approach

Use a queue to perform a level-order traversal. Process all nodes currently in the queue before moving to the next level, storing the values of each level separately in the final result.

#### What I Learned

- Breadth-First Search (BFS)
- Queue implementation using `deque`
- Level-by-level traversal
- Processing nodes in the correct order

#### Difficulty Faced

Understanding why storing the queue size before each iteration ensures that nodes belonging to the same level are processed together.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(n)

---

## Overall Learning

Today's problems introduced two important Binary Tree traversal techniques. I learned how recursion can be used to compute tree properties such as the diameter, while Breadth-First Search provides an efficient way to process nodes level by level. Understanding when to use DFS versus BFS is becoming an important part of solving tree problems effectively.

## Status

✅ Both problems accepted on LeetCode

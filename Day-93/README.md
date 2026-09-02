# Day 93 - Longest Univalue Path & All Nodes Distance K in Binary Tree

## Problems

### 1. LeetCode 687 - Longest Univalue Path

**Topic:** Binary Trees, DFS, Recursion

### Approach

Use DFS to calculate the longest path that can extend from each node through children having the same value.

For every node, calculate the valid path through its left and right children and update the maximum diameter found.

Only the longer of the two paths is returned to the parent because a path extending upward cannot branch in both directions.

### What I Learned

- Using DFS to calculate subtree information
- Finding paths through a binary tree
- Combining information from left and right subtrees
- Understanding how recursive results can be used at the parent node

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 863 - All Nodes Distance K in Binary Tree

**Topic:** Binary Trees, BFS, DFS, Graphs

### Approach

Convert the binary tree into an undirected graph so that movement is possible between a node and its parent as well as its children.

Then perform BFS starting from the target node.

When the distance reaches `k`, all nodes at that level are included in the result.

### What I Learned

- Converting a tree into a graph representation
- Moving both upward and downward in a tree
- Using BFS to find nodes at an exact distance
- Tracking visited nodes to avoid revisiting nodes

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems showed two different ways of thinking about binary trees.

The first problem used DFS to gather information from subtrees and build the longest valid path. The second changed the representation of the tree into an undirected graph to make movement in both directions possible.

The biggest takeaway was that **choosing the right traversal and representation can make a difficult tree problem much easier to solve.**

## Status

✅ Both problems accepted on LeetCode.

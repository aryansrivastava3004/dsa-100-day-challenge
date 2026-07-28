# Day 57 - Sum of Left Leaves & Minimum Depth of Binary Tree

## Problems

### 1. LeetCode 404 - Sum of Left Leaves

**Topic:** Binary Tree, Depth-First Search (DFS), Recursion

### Approach

Traverse the tree using DFS while passing a boolean flag to indicate whether the current node is a left child. Whenever a left leaf node is encountered, add its value to the total sum. Continue recursively for both left and right subtrees.

### What I Learned

- Passing additional information during recursive calls
- Identifying left leaf nodes correctly
- Using DFS for conditional tree traversal
- Strengthening recursive thinking in Binary Trees

### Difficulty Faced

Understanding the difference between a left child and a left leaf node, as only left leaves contribute to the answer.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 111 - Minimum Depth of Binary Tree

**Topic:** Binary Tree, Depth-First Search (DFS), Recursion

### Approach

Use recursion to compute the minimum depth from the root to the nearest leaf node. Special care is taken when a node has only one child to avoid considering a missing subtree as having zero depth.

### What I Learned

- Finding the shortest root-to-leaf path
- Handling trees with a single child correctly
- Comparing subtree depths recursively
- Managing important edge cases in Binary Trees

### Difficulty Faced

Avoiding the common mistake of directly taking the minimum depth when one subtree is missing, which leads to incorrect results.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems improved my understanding of Binary Tree recursion by focusing on node properties and tree depth. I learned how a small change in recursive logic can solve entirely different problems. Handling edge cases carefully is just as important as implementing the algorithm itself, especially in tree-based questions.

## Status

✅ Both problems accepted on LeetCode.

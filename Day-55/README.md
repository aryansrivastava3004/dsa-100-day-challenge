# Day 55 - Binary Tree Preorder Traversal & Binary Tree Postorder Traversal

## Problems

### 1. LeetCode 144 - Binary Tree Preorder Traversal

**Topic:** Binary Tree, Depth-First Search (DFS), Recursion

### Approach

Traverse the tree recursively using **Preorder Traversal (Root → Left → Right)**. Visit the current node first, then recursively traverse the left subtree followed by the right subtree, storing each visited node in the result list.

### What I Learned

- Preorder traversal follows **Root → Left → Right**
- Recursive DFS implementation
- Processing the current node before its children
- Building traversal results recursively

### Difficulty Faced

Initially, it was easy to confuse preorder with inorder traversal. Practicing the traversal order helped reinforce the correct sequence.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 145 - Binary Tree Postorder Traversal

**Topic:** Binary Tree, Depth-First Search (DFS), Recursion

### Approach

Traverse the tree recursively using **Postorder Traversal (Left → Right → Root)**. Visit both child subtrees before processing the current node and adding its value to the result.

### What I Learned

- Postorder traversal follows **Left → Right → Root**
- Processing child nodes before the parent
- Recursive DFS traversal
- Understanding scenarios where postorder traversal is useful

### Difficulty Faced

Remembering to process the root only after both subtrees have been completely traversed.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems completed my understanding of the three fundamental Depth-First Search traversals in Binary Trees: **Preorder, Inorder, and Postorder**. I learned how changing the order in which nodes are processed leads to different traversal strategies, each suited for different types of problems. Mastering these traversal patterns will make more advanced tree problems easier to solve.

## Status

✅ Both problems accepted on LeetCode.

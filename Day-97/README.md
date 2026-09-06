# Day 97 - N-ary Tree Level Order Traversal & N-ary Tree Postorder Traversal

## Problems

### 1. LeetCode 429 - N-ary Tree Level Order Traversal

**Topic:** N-ary Tree, BFS, Queue

### Approach

Use Breadth-First Search with a queue.

For every level, process all nodes currently present in the queue and store their values. Then add all their children to the queue for the next level.

### What I Learned

- Level order traversal of an N-ary Tree
- Using BFS with a queue
- Processing a tree level by level
- Handling multiple children for each node

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 590 - N-ary Tree Postorder Traversal

**Topic:** N-ary Tree, DFS, Recursion

### Approach

Use Depth-First Search and recursively visit every child before adding the current node to the result.

Postorder traversal follows:

Children → Root

### What I Learned

- Postorder traversal of an N-ary Tree
- Using DFS and recursion
- Processing multiple children recursively
- Applying tree traversal concepts to N-ary Trees

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems focused on two fundamental tree traversal techniques.

The first problem used BFS to process an N-ary Tree level by level, while the second used DFS to process all children before the current node.

Working with N-ary Trees showed how the same traversal concepts used for binary trees can be extended to trees with any number of children.

## Status

✅ Both problems accepted on LeetCode.

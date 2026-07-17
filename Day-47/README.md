# Day 47 - Invert Binary Tree & Flood Fill

## Problems

### 1. LeetCode 226 - Invert Binary Tree

**Topic:** Binary Tree, Depth-First Search (DFS), Recursion

### Approach

Starting from the root, recursively swap the left and right child of every node. Continue the process until all nodes have been visited, effectively mirroring the entire tree.

### What I Learned

- Recursive tree traversal
- Swapping child nodes in-place
- Tree transformation using DFS
- Strengthened understanding of recursion on binary trees

### Difficulty Faced

Initially, it was slightly confusing that simply swapping the children at every recursive call would eventually invert the whole tree, but visualizing the recursion made it much clearer.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 733 - Flood Fill

**Topic:** Graphs, DFS, Matrix Traversal

### Approach

Start DFS from the given pixel. Change its color and recursively visit all four adjacent cells that have the original color while staying within the image boundaries.

### What I Learned

- Applying DFS on a 2D grid
- Boundary checking
- Recursive graph traversal
- Importance of checking if the new color equals the original color

### Difficulty Faced

Managing all boundary conditions correctly and understanding why revisiting already-colored cells must be avoided.

### Complexity

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)

---

## Overall Learning

Today's problems demonstrated how the same recursion concept can solve two completely different problems. Invert Binary Tree strengthened my understanding of recursive tree traversal, while Flood Fill introduced graph traversal on a matrix using DFS. This was an excellent bridge from Binary Trees to Graph algorithms.

## Status

✅ Both problems accepted on LeetCode.

# Day 73 - Surrounded Regions & Pacific Atlantic Water Flow

## Problems

### 1. LeetCode 130 - Surrounded Regions

**Topic:** Graphs, DFS, Matrix Traversal

### Approach

Instead of searching for regions that are surrounded, start from the boundary cells. Any `O` connected to the boundary cannot be surrounded.

Temporarily mark all boundary-connected `O` cells as `#`. Then:

- Convert remaining `O` cells to `X`.
- Convert `#` cells back to `O`.

### What I Learned

- Using DFS for connected components in a matrix
- Starting traversal from boundaries
- Solving problems using the opposite perspective
- Modifying a matrix in-place

### Complexity

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)

---

### 2. LeetCode 417 - Pacific Atlantic Water Flow

**Topic:** Graphs, DFS, Matrix Traversal

### Approach

Instead of starting from every cell and checking whether water can reach both oceans, reverse the direction of the problem.

Run DFS from:

- Pacific Ocean boundaries
- Atlantic Ocean boundaries

During reverse traversal, move to neighboring cells whose height is greater than or equal to the current cell.

Any cell reachable from both oceans is part of the answer.

### What I Learned

- Reverse graph traversal
- Running DFS from multiple starting points
- Using sets to track reachable cells
- Recognizing when reversing a problem makes it simpler

### Complexity

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)

---

## Overall Learning

Today's problems strengthened my understanding of DFS on 2D grids. More importantly, they taught me that the direction from which a problem is approached can completely change its difficulty.

For **Surrounded Regions**, starting from the boundary identifies the cells that should remain untouched. For **Pacific Atlantic Water Flow**, starting from the oceans eliminates the need to perform a search from every individual cell.

The biggest takeaway was:

**Sometimes the best way to solve a problem is to solve its reverse.**

## Status

✅ Both problems accepted on LeetCode.

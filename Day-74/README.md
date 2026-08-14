# Day 74 - Max Area of Island & Rotting Oranges

## Problems

### 1. LeetCode 695 - Max Area of Island

**Topic:** Graphs, DFS, Matrix Traversal

### Approach

Treat every group of connected `1`s as an island. Whenever an unvisited land cell is found, perform DFS to explore the complete island and count its area.

The visited cells are changed from `1` to `0` so that the same island is not processed again.

### What I Learned

- Using DFS to find connected components
- Calculating the size of a connected region
- Traversing a 2D grid as a graph
- Modifying the grid in-place to track visited cells

### Complexity

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)

---

### 2. LeetCode 994 - Rotting Oranges

**Topic:** Graphs, BFS, Multi-Source BFS, Matrix Traversal

### Approach

Initially add every rotten orange to a queue. Since all rotten oranges spread simultaneously, this becomes a Multi-Source BFS problem.

Each BFS level represents one minute. During each level, every rotten orange attempts to rot its adjacent fresh oranges.

After BFS finishes, if fresh oranges remain, return `-1`; otherwise return the number of minutes required.

### What I Learned

- Understanding Multi-Source BFS
- Using BFS levels to represent time
- Processing multiple starting points simultaneously
- Tracking the number of remaining fresh nodes

### Complexity

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)

---

## Overall Learning

Today's problems strengthened my understanding of **DFS and BFS on 2D grids**.

Max Area of Island demonstrated how DFS can be used to explore and measure connected components, while Rotting Oranges showed how Multi-Source BFS can model a process that spreads simultaneously from multiple starting points.

The key takeaway was understanding **when to choose DFS and when to choose BFS** based on the nature of the problem.

## Status

✅ Both problems accepted on LeetCode.

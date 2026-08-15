# Day 75 - Shortest Path in Binary Matrix & 01 Matrix

## Problems

### 1. LeetCode 1091 - Shortest Path in Binary Matrix

**Topic:** Graphs, BFS, Grid Traversal, Shortest Path

### Approach

Treat every cell as a node in a graph. Since every move has the same cost, BFS can be used to find the shortest path.

The problem allows movement in all 8 directions, including diagonals. The first time the bottom-right cell is reached, the shortest path has been found.

### What I Learned

- Using BFS for shortest-path problems
- Traversing grids in 8 directions
- Understanding why BFS finds the shortest path in unweighted graphs
- Tracking distance level by level

### Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n²)

---

### 2. LeetCode 542 - 01 Matrix

**Topic:** Graphs, Multi-Source BFS, Matrix Traversal

### Approach

Instead of running BFS separately from every `1`, start BFS simultaneously from every `0`.

Each `0` acts as a source. As BFS expands, the first time an unvisited cell is reached represents its minimum distance from any `0`.

### What I Learned

- Multi-Source BFS
- Calculating minimum distance to multiple sources
- Using BFS levels to represent distance
- Recognizing when multiple starting points should be processed simultaneously

### Complexity

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)

---

## Overall Learning

Today's problems strengthened my understanding of BFS as a shortest-path technique for unweighted graphs.

The first problem used BFS to find a shortest route through a binary matrix, while the second used Multi-Source BFS to calculate the minimum distance from every cell to the nearest `0`.

The biggest takeaway was understanding that many seemingly different grid problems are simply different applications of the same BFS pattern.

## Status

✅ Both problems accepted on LeetCode.

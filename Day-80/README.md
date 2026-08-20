# Day 80 - Reorder Routes to Make All Paths Lead to the City Zero & Nearest Exit from Entrance in Maze

## Problems

### 1. LeetCode 1466 - Reorder Routes to Make All Paths Lead to the City Zero

**Topic:** Graphs, DFS, Directed Graph

### Approach

Convert the directed graph into an undirected representation while storing whether each edge needs to be reversed.

- `1` means the original road points away from city `0` and needs to be reversed.
- `0` means the road already points towards city `0`.

Start DFS from city `0` and count every edge that needs to be reversed.

### What I Learned

- Representing directed edges in an undirected traversal structure
- Using DFS to count required edge reversals
- Tracking additional information with graph edges
- Understanding how edge direction affects graph traversal

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 1926 - Nearest Exit from Entrance in Maze

**Topic:** BFS, Grid Traversal, Shortest Path

### Approach

Start BFS from the entrance and explore the maze level by level.

Each BFS level represents one additional step. Since all movements have the same cost, the first boundary cell reached is guaranteed to be the nearest exit.

The entrance itself is not considered an exit.

### What I Learned

- Using BFS to find the shortest path in a grid
- Tracking distance during BFS
- Identifying boundary cells as destinations
- Marking visited cells to avoid repeated traversal

### Complexity

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)

---

## Overall Learning

Today's problems demonstrated two different applications of graph traversal.

**Reorder Routes** used DFS to reason about edge directions and count the minimum number of reversals, while **Nearest Exit from Entrance in Maze** used BFS to find the shortest path through a grid.

The biggest takeaway was understanding that the choice between DFS and BFS depends on what the problem is asking us to calculate.

## Status

✅ Both problems accepted on LeetCode.

# Day 67 - Network Delay Time & Path With Minimum Effort

## Problems

### 1. LeetCode 743 - Network Delay Time

**Topic:** Graphs, Dijkstra's Algorithm, Priority Queue

### Approach

Represent the graph using an adjacency list and apply Dijkstra's Algorithm with a Min Heap. Always process the node with the smallest known travel time. Once a node is removed from the heap for the first time, its shortest distance is finalized. Track the maximum arrival time among all reachable nodes. If every node is visited, return the maximum time; otherwise, return `-1`.

### What I Learned

- Implementing Dijkstra's Algorithm
- Representing weighted graphs with adjacency lists
- Using Min Heaps for shortest path problems
- Understanding when a shortest path becomes final

### Difficulty Faced

Understanding why the first time a node is removed from the Min Heap, its shortest distance is guaranteed to be the minimum possible.

### Complexity

- **Time Complexity:** O((V + E) log V)
- **Space Complexity:** O(V + E)

---

### 2. LeetCode 1631 - Path With Minimum Effort

**Topic:** Graphs, Dijkstra's Algorithm, Grid Traversal

### Approach

Treat each cell as a graph node and apply Dijkstra's Algorithm. Instead of minimizing the total distance, minimize the maximum height difference encountered along the path. Maintain an effort matrix to store the minimum effort required to reach each cell and use a Min Heap to always process the path with the smallest current effort.

### What I Learned

- Applying Dijkstra's Algorithm on grids
- Using custom cost functions
- Maintaining minimum effort for every cell
- Solving shortest-path style problems beyond simple distances

### Difficulty Faced

Realizing that the path cost is defined by the **maximum edge weight** instead of the sum of edge weights, which changes how the algorithm updates distances.

### Complexity

- **Time Complexity:** O(mn log(mn))
- **Space Complexity:** O(mn)

---

## Overall Learning

Today's problems introduced one of the most important graph algorithms—**Dijkstra's Algorithm**. I learned how a Min Heap helps efficiently process the next optimal node and how the same algorithm can be adapted to different cost functions. Whether minimizing travel time in a graph or minimizing the maximum effort in a grid, the core idea remains the same: always expand the most promising path first.

## Status

✅ Both problems accepted on LeetCode.

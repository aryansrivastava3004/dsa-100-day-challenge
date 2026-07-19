# Day 48 - Number of Islands & Find if Path Exists in Graph

## Problems

### 1. LeetCode 200 - Number of Islands

**Topic:** Graphs, Depth-First Search (DFS), Matrix Traversal

### Approach

Traverse the grid cell by cell. Whenever an unvisited land cell (`'1'`) is found, start a DFS to mark all connected land cells as visited by converting them to water (`'0'`). Each new DFS represents a separate island.

### What I Learned

- Counting connected components using DFS
- Traversing a 2D grid recursively
- Marking visited cells in-place
- Applying graph traversal concepts to matrices

### Difficulty Faced

Understanding that one DFS call explores an entire connected island, preventing duplicate counting.

### Complexity

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)

---

### 2. LeetCode 1971 - Find if Path Exists in Graph

**Topic:** Graphs, DFS, Adjacency List

### Approach

Convert the edge list into an adjacency list. Starting from the source node, perform a DFS while maintaining a visited set. If the destination node is reached, return `True`; otherwise, continue exploring until all reachable nodes are visited.

### What I Learned

- Building an adjacency list
- DFS traversal on graphs
- Preventing infinite loops using a visited set
- Checking connectivity between two nodes

### Difficulty Faced

Understanding how the graph is represented internally using an adjacency list and why revisiting nodes must be avoided.

### Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)

---

## Overall Learning

Today's problems strengthened my understanding of graph traversal using Depth-First Search. I learned how DFS can be applied both to matrix-based problems like **Number of Islands** and to general graphs using adjacency lists. These problems reinforced the concept of connected components and graph connectivity, which are fundamental topics in graph algorithms.

## Status

✅ Both problems accepted on LeetCode.

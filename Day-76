# Day 76 - Is Graph Bipartite? & Clone Graph

## Problems

### 1. LeetCode 785 - Is Graph Bipartite?

**Topic:** Graphs, BFS, Graph Coloring

### Approach

Use BFS to color the graph using two colors. Every neighboring node must receive the opposite color.

If two connected nodes ever have the same color, the graph cannot be bipartite.

Since the graph may contain multiple disconnected components, BFS is started from every unvisited node.

### What I Learned

- Understanding bipartite graphs
- Graph coloring using BFS
- Handling disconnected graph components
- Detecting conflicts between neighboring nodes

### Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V)

---

### 2. LeetCode 133 - Clone Graph

**Topic:** Graphs, DFS, Hash Map

### Approach

Use DFS to traverse the original graph while maintaining a Hash Map that maps every original node to its cloned node.

Before cloning a node, check whether it already exists in the map. This prevents infinite recursion when the graph contains cycles.

### What I Learned

- Cloning graph structures
- Using DFS for graph traversal
- Handling cycles using a visited Hash Map
- Mapping original objects to their copies

### Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V)

---

## Overall Learning

Today's problems strengthened my understanding of graph traversal and state management.

For **Is Graph Bipartite?**, I used BFS with graph coloring to detect conflicts between connected nodes. For **Clone Graph**, I used DFS with a Hash Map to safely create an independent copy of a graph containing possible cycles.

The biggest takeaway was that **properly tracking visited nodes is essential when working with graphs**, especially when cycles or disconnected components are involved.

## Status

✅ Both problems accepted on LeetCode.

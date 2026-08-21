# Day 81 - Keys and Rooms & Possible Bipartition

## Problems

### 1. LeetCode 841 - Keys and Rooms

**Topic:** Graphs, DFS, Graph Traversal

### Approach

Treat each room as a graph node and every key as a directed edge to another room.

Start DFS from room `0` and recursively visit every room whose key can be obtained.

If all rooms are visited, return `True`; otherwise, return `False`.

### What I Learned

- Representing real-world relationships as graphs
- Using DFS to find reachable nodes
- Tracking visited nodes
- Recognizing directed graph traversal problems

### Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V)

---

### 2. LeetCode 886 - Possible Bipartition

**Topic:** Graphs, BFS, Bipartite Graph, Graph Coloring

### Approach

Treat every person as a graph node and every dislike relationship as an undirected edge.

Use BFS to color the graph using two colors. People connected by a dislike relationship must receive opposite colors.

If two connected people ever receive the same color, a valid bipartition is impossible.

### What I Learned

- Applying graph coloring to real-world problems
- Detecting bipartite graphs using BFS
- Handling disconnected graph components
- Reusing the two-coloring pattern

### Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)

---

## Overall Learning

Today's problems showed how graph algorithms can be hidden behind completely different problem statements.

Keys and Rooms is essentially a graph reachability problem, while Possible Bipartition is a graph-coloring problem.

The biggest takeaway was learning to look beyond the story and identify the underlying structure of the problem.

## Status

✅ Both problems accepted on LeetCode.

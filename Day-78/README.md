# Day 78 - Find Eventual Safe States & Minimum Height Trees

## Problems

### 1. LeetCode 802 - Find Eventual Safe States

**Topic:** Graphs, Topological Sort, BFS, Reverse Graph

### Approach

Build a reverse graph and track the outdegree of every node.

Terminal nodes have an outdegree of `0`, so they are safe. Starting from these nodes, work backwards and reduce the outdegree of their predecessors.

Whenever a predecessor's outdegree becomes `0`, it is also safe.

Nodes that never become safe are part of a cycle or can eventually reach a cycle.

### What I Learned

- Building reverse graphs
- Applying Topological Sort to cycle-related problems
- Using outdegree instead of indegree
- Identifying nodes that cannot reach a cycle

### Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)

---

### 2. LeetCode 310 - Minimum Height Trees

**Topic:** Graphs, BFS, Topological Sort, Tree

### Approach

The centers of a tree produce the minimum possible height.

Instead of checking every node as a possible root, repeatedly remove all leaf nodes from the outside of the tree.

Continue removing layers until only one or two nodes remain. These remaining nodes are the center(s) of the tree.

### What I Learned

- Finding the center of a tree
- Layer-by-layer BFS
- Repeatedly removing leaf nodes
- Applying Topological Sort-like ideas to undirected trees

### Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)

---

## Overall Learning

Today's problems showed how the same graph concepts can be applied in very different ways.

For **Find Eventual Safe States**, I worked backwards from terminal nodes using a reverse graph. For **Minimum Height Trees**, I repeatedly removed the outermost leaf nodes until only the center remained.

The biggest takeaway was learning to recognize the common pattern of **removing nodes layer by layer to reveal the important nodes underneath**.

## Status

✅ Both problems accepted on LeetCode.

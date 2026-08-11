# Day 71 - Redundant Connection II & Number of Operations to Make Network Connected

## Problems

### 1. LeetCode 685 - Redundant Connection II

**Topic:** Graphs, Union-Find, Directed Graph

### Approach

The problem can have two possible issues:

1. A node may have two parents.
2. The graph may contain a cycle.

First, identify whether any node has two incoming edges. Then use Union-Find while temporarily skipping the second incoming edge. Based on whether a cycle is detected, determine which edge must be removed.

### What I Learned

- Applying Union-Find to directed graphs
- Detecting nodes with multiple parents
- Detecting cycles simultaneously
- Handling multiple possible invalid configurations
- Extending the standard Redundant Connection approach

### Complexity

- **Time Complexity:** O(n α(n))
- **Space Complexity:** O(n)

---

### 2. LeetCode 1319 - Number of Operations to Make Network Connected

**Topic:** Graphs, Union-Find, Connected Components

### Approach

First, check whether there are enough cables to connect all `n` computers. At least `n - 1` connections are required.

Then use Union-Find to determine the number of connected components. Every successful union reduces the number of components by one. Therefore, the number of operations required is `components - 1`.

### What I Learned

- Counting connected components using DSU
- Understanding the minimum number of edges required for connectivity
- Detecting redundant connections
- Using path compression and union by rank

### Complexity

- **Time Complexity:** O(E α(n))
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems strengthened my understanding of **Union-Find / Disjoint Set Union** by applying it to both directed and undirected graph problems.

I learned that DSU can be used for much more than simple cycle detection. It can identify connected components, handle redundant connections, and help solve complex graph connectivity problems efficiently.

## Status

✅ Both problems accepted on LeetCode.

# Day 70 - Min Cost to Connect All Points & Redundant Connection

## Problems

### 1. LeetCode 1584 - Min Cost to Connect All Points

**Topic:** Graphs, Minimum Spanning Tree, Prim's Algorithm, Heap

### Approach

Use Prim's Algorithm to construct a Minimum Spanning Tree. Start from any point and use a Min Heap to always select the minimum-cost edge connecting a new point to the already connected component.

The cost between two points is their Manhattan distance:

`|x1 - x2| + |y1 - y2|`

Continue until every point has been connected.

### What I Learned

- Understanding Minimum Spanning Trees
- Implementing Prim's Algorithm
- Using a Min Heap for MST construction
- Calculating Manhattan distance
- Understanding the difference between MST and shortest-path problems

### Complexity

- **Time Complexity:** O(n² log n)
- **Space Complexity:** O(n²)

---

### 2. LeetCode 684 - Redundant Connection

**Topic:** Graphs, Union-Find, Disjoint Set Union (DSU)

### Approach

Use the Union-Find data structure to detect when adding an edge creates a cycle.

For every edge, find the root of both nodes. If both nodes already belong to the same component, adding the edge would create a cycle, making that edge the redundant connection.

Path compression and union by rank are used to keep the operations efficient.

### What I Learned

- Understanding Union-Find / DSU
- Detecting cycles in undirected graphs
- Path compression
- Union by rank
- Understanding how DSU is used in Kruskal's Algorithm

### Complexity

- **Time Complexity:** O(n α(n))
- **Space Complexity:** O(n)

> `α(n)` is the inverse Ackermann function and is effectively constant for practical input sizes.

---

## Overall Learning

Today's problems introduced two important graph concepts: **Minimum Spanning Trees** and **Disjoint Set Union**.

I learned that graph problems aren't always about finding the shortest path. Sometimes the goal is to connect every node with minimum total cost, while other problems require detecting whether adding an edge creates a cycle.

Prim's Algorithm and Union-Find provided two very different approaches to graph connectivity, reinforcing the importance of identifying the correct pattern before choosing an algorithm.

## Status

✅ Both problems accepted on LeetCode.

# Day 68 - Path with Maximum Probability & Cheapest Flights Within K Stops

## Problems

### 1. LeetCode 1514 - Path with Maximum Probability

**Topic:** Graphs, Dijkstra's Algorithm, Priority Queue

### Approach

Represent the graph using an adjacency list and use a Max Heap to always process the path with the highest probability. Since Python provides a Min Heap, negative probabilities are stored to simulate a Max Heap. The probability of reaching a neighboring node is calculated by multiplying the current probability by the edge probability.

### What I Learned

- Adapting Dijkstra's Algorithm to maximize probability
- Using a Max Heap with negative values
- Multiplying probabilities along a path
- Applying shortest-path concepts to different optimization problems

### Difficulty Faced

Understanding how Dijkstra's idea can be modified when the goal is to maximize a product rather than minimize a sum.

### Complexity

- **Time Complexity:** O((V + E) log V)
- **Space Complexity:** O(V + E)

---

### 2. LeetCode 787 - Cheapest Flights Within K Stops

**Topic:** Graphs, Priority Queue, Shortest Path

### Approach

Represent the flights using an adjacency list and use a Min Heap containing the current cost, node, and number of stops. Each state is tracked using `(node, stops)` because reaching the same node with different numbers of stops represents different possibilities.

### What I Learned

- Combining Priority Queues with constraints
- Tracking multiple values as a graph state
- Understanding constrained shortest-path problems
- Modifying Dijkstra-style approaches according to problem requirements

### Difficulty Faced

Understanding why the number of stops must be included in the state instead of tracking only the minimum cost for each node.

### Complexity

- **Time Complexity:** O(E log E)
- **Space Complexity:** O(V + E)

---

## Overall Learning

Today's problems showed how graph algorithms can be adapted to handle different optimization goals and additional constraints. I learned that the underlying idea of Dijkstra's Algorithm can be extended beyond traditional shortest paths by changing the priority metric or adding extra state information.

The biggest takeaway was that **understanding the algorithmic pattern is more important than memorizing one implementation**.

## Status

✅ Both problems accepted on LeetCode.

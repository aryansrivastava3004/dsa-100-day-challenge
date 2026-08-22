# Day 82 - Snakes and Ladders & Shortest Bridge

## Problems

### 1. LeetCode 909 - Snakes and Ladders

**Topic:** Graphs, BFS, Shortest Path, Matrix Traversal

### Approach

Treat every square on the board as a graph node. From each square, we can move to the next 1–6 squares based on the dice roll.

If a square contains a snake or ladder, the destination changes accordingly.

Since every dice roll has the same cost, BFS guarantees the minimum number of moves needed to reach the final square.

### What I Learned

- Representing a board game as a graph
- Using BFS for minimum moves
- Handling special transitions
- Converting a 2D board into a 1D sequence of graph states

### Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n²)

---

### 2. LeetCode 934 - Shortest Bridge

**Topic:** Graphs, DFS, BFS, Multi-Source BFS

### Approach

First use DFS to find and mark the first island. At the same time, add all cells belonging to that island into a queue.

Then perform BFS from all these cells simultaneously. Each BFS layer represents one additional water cell crossed.

The first time the BFS reaches the second island, the current distance is the shortest bridge.

### What I Learned

- Combining DFS and BFS in one problem
- Finding connected components with DFS
- Applying Multi-Source BFS
- Finding the shortest distance between two components

### Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n²)

---

## Overall Learning

Today's problems showed two very different applications of BFS.

In **Snakes and Ladders**, the board was transformed into a graph and BFS found the minimum number of moves.

In **Shortest Bridge**, DFS first identified one connected component, and BFS then found the shortest distance to the other component.

The biggest takeaway was learning that **different graph patterns can be combined to solve a single problem efficiently**.

## Status

✅ Both problems accepted on LeetCode.

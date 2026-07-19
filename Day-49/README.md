# Day 49 - Binary Tree Paths & Number of Provinces

## Problems

### 1. LeetCode 257 - Binary Tree Paths

**Topic:** Binary Tree, Depth-First Search (DFS), Recursion

### Approach

Perform a Depth-First Search starting from the root while maintaining the current path as a string. Whenever a leaf node is reached, add the complete root-to-leaf path to the answer.

### What I Learned

- Constructing root-to-leaf paths using recursion
- Passing state (current path) through recursive calls
- Identifying leaf nodes efficiently
- Strengthening DFS traversal on Binary Trees

### Difficulty Faced

Understanding that each recursive call gets its own copy of the current path, allowing different branches to be explored independently.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 547 - Number of Provinces

**Topic:** Graphs, DFS, Connected Components

### Approach

Treat each city as a graph node represented by an adjacency matrix. For every unvisited city, perform DFS to visit all directly or indirectly connected cities. Each DFS traversal represents one province.

### What I Learned

- Finding connected components in graphs
- DFS traversal using an adjacency matrix
- Managing visited nodes efficiently
- Counting disconnected groups within a graph

### Difficulty Faced

Recognizing that each unvisited city starts a new DFS traversal and represents a new province.

### Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems reinforced the versatility of Depth-First Search. In **Binary Tree Paths**, DFS was used to construct every root-to-leaf path, while in **Number of Provinces**, it helped identify connected components in a graph represented by an adjacency matrix. These problems strengthened my understanding of how the same traversal technique can solve different classes of problems by adapting to the underlying data structure.

## Status

✅ Both problems accepted on LeetCode.

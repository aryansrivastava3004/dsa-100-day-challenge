# Day 69 - Number of Ways to Arrive at Destination & Second Minimum Time to Reach Destination

## Problems

### 1. LeetCode 1976 - Number of Ways to Arrive at Destination

**Topic:** Graphs, Dijkstra's Algorithm, Shortest Path

### Approach

Use Dijkstra's Algorithm while maintaining two arrays:

- `dist` stores the shortest time to reach each node.
- `ways` stores the number of different shortest paths to each node.

When a shorter path is found, replace the existing path count. When another path with exactly the same shortest distance is found, add its number of ways to the existing count.

### What I Learned

- Extending Dijkstra's Algorithm beyond finding distances
- Counting multiple shortest paths
- Maintaining additional information during graph traversal
- Using modulo arithmetic for large results

### Complexity

- **Time Complexity:** O((V + E) log V)
- **Space Complexity:** O(V + E)

---

### 2. LeetCode 2045 - Second Minimum Time to Reach Destination

**Topic:** Graphs, Shortest Path, BFS

### Approach

Maintain the two smallest arrival times for every node. While traversing the graph, calculate the actual arrival time by considering both the travel time and the current traffic-light state.

If a newly calculated time is the shortest, update the first distance. If it is greater than the shortest but smaller than the current second-best distance, update the second distance.

### What I Learned

- Finding the second shortest arrival time
- Maintaining multiple distances for each node
- Handling traffic-light timing constraints
- Extending shortest-path concepts to more complex states

### Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)

---

## Overall Learning

Today's problems showed that shortest-path algorithms can be extended far beyond simply finding the minimum distance. I learned how to count multiple shortest paths and how to track both the shortest and second-shortest arrival times while handling additional constraints.

The biggest takeaway was that **Dijkstra and BFS are patterns that can be adapted rather than fixed algorithms**. By storing additional information with each state, the same fundamental ideas can solve much more complex graph problems.

## Status

✅ Both problems accepted on LeetCode.

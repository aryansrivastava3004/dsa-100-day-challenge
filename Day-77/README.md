# Day 77 - Course Schedule & Course Schedule II

## Problems

### 1. LeetCode 207 - Course Schedule

**Topic:** Graphs, Topological Sort, BFS, Cycle Detection

### Approach

Represent the prerequisites as a directed graph and calculate the indegree of every course.

Courses with an indegree of `0` have no remaining prerequisites and can be processed immediately. After processing a course, reduce the indegree of its dependent courses.

If all courses can be processed, the graph contains no cycle and all courses can be completed.

### What I Learned

- Understanding Topological Sorting
- Using Kahn's Algorithm
- Detecting cycles in directed graphs
- Using indegrees to represent dependencies
- Processing nodes whose dependencies are completed

### Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)

---

### 2. LeetCode 210 - Course Schedule II

**Topic:** Graphs, Topological Sort, BFS, Cycle Detection

### Approach

Use the same Topological Sort approach as Course Schedule, but instead of only checking whether all courses can be completed, store every processed course in an `order` list.

If all courses appear in the ordering, return it. Otherwise, a cycle exists and no valid ordering is possible.

### What I Learned

- Producing a topological ordering
- Reusing an algorithmic pattern for a related problem
- Detecting impossible schedules using cycle detection
- Understanding the relationship between feasibility and ordering problems

### Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)

---

## Overall Learning

Today's problems were a great example of **pattern recognition**.

Course Schedule asks whether a valid ordering exists, while Course Schedule II asks us to actually produce that ordering. Both problems use the same underlying Topological Sort pattern.

The biggest takeaway was that once the core algorithm is understood, related problems become much easier to approach.

## Status

✅ Both problems accepted on LeetCode.

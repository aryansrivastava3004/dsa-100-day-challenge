# Day 72 - Evaluate Division & Accounts Merge

## Problems

### 1. LeetCode 399 - Evaluate Division

**Topic:** Graphs, DFS, Weighted Graph

### Approach

Represent each equation as a weighted graph.

For an equation `a / b = value`:

- Add an edge from `a` to `b` with weight `value`.
- Add an edge from `b` to `a` with weight `1 / value`.

For each query, perform DFS to find a path from the starting variable to the target variable. Multiply the edge weights along the path to obtain the result.

### What I Learned

- Representing mathematical relationships as graphs
- Building weighted graphs
- Using DFS to evaluate relationships
- Multiplying edge weights along a path
- Detecting unreachable variables

### Difficulty Faced

Understanding how a division equation can be transformed into a graph where the edge weights represent the relationship between variables.

### Complexity

- **Time Complexity:** O(Q × (V + E))
- **Space Complexity:** O(V + E)

---

### 2. LeetCode 721 - Accounts Merge

**Topic:** Union-Find, Disjoint Set Union, Connected Components

### Approach

Treat every email address as a node. Emails belonging to the same account are connected using Union-Find.

For every account, connect all its emails to the first email. After processing all accounts, emails with the same root belong to the same person. Group the emails by their root, sort them, and attach the corresponding name.

### What I Learned

- Applying Union-Find to real-world data
- Finding connected components using DSU
- Using path compression
- Using union by rank
- Combining DSU with sorting

### Difficulty Faced

Understanding why connecting every email to the first email of an account is enough to merge all accounts that share common emails.

### Complexity

- **Time Complexity:** O(N log N)
- **Space Complexity:** O(N)

> **N = Total number of email addresses**

---

## Overall Learning

Today's problems showed how graph concepts can be hidden inside completely different problem statements.

**Evaluate Division** transformed mathematical relationships into a weighted graph and used DFS to find the required relationships. **Accounts Merge** turned account information into connected components and used Union-Find to combine related data.

The biggest takeaway was learning to look beyond the surface of a problem and identify the underlying data structure and algorithmic pattern.

## Status

✅ Both problems accepted on LeetCode.

# Day 59 - Populating Next Right Pointers in Each Node II & Flatten Binary Tree to Linked List

## Problems

### 1. LeetCode 117 - Populating Next Right Pointers in Each Node II

**Topic:** Binary Tree, Breadth-First Search (BFS), Queue

### Approach

Perform a level-order traversal using a queue. For each level, connect every node to its immediate right neighbor using the `next` pointer. Since the tree is not necessarily perfect, process only the existing child nodes while traversing.

### What I Learned

- Connecting nodes in a general Binary Tree
- Applying BFS to non-perfect trees
- Processing one level completely before moving to the next
- Reusing level-order traversal for tree modification

### Difficulty Faced

Handling missing child nodes while ensuring the `next` pointers are connected correctly across each level.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

### 2. LeetCode 114 - Flatten Binary Tree to Linked List

**Topic:** Binary Tree, Depth-First Search (DFS), Recursion

### Approach

Traverse the tree in reverse preorder (**Right → Left → Root**). Maintain a pointer to the previously processed node and update each node's right pointer to create a linked list while setting the left pointer to `None`.

### What I Learned

- Reverse preorder traversal
- Modifying Binary Trees in-place
- Rearranging pointers recursively
- Using DFS for tree transformation

### Difficulty Faced

Understanding why traversing in reverse preorder makes it possible to flatten the tree efficiently without requiring additional data structures.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems introduced me to modifying Binary Trees rather than simply traversing them. I learned how BFS can be used to connect nodes level by level, while DFS can completely transform a tree into a linked list. These problems reinforced the importance of choosing the right traversal order depending on the desired outcome.

## Status

✅ Both problems accepted on LeetCode.

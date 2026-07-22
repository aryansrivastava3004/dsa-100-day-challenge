# Day 52 - Lowest Common Ancestor of a Binary Search Tree & Lowest Common Ancestor of a Binary Tree

## Problems

### 1. LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree

**Topic:** Binary Search Tree (BST), Tree Traversal

### Approach

Use the BST property to compare the values of the two target nodes with the current node. If both nodes are smaller, move left. If both are larger, move right. The first node where the paths diverge (or where one node equals the current node) is the Lowest Common Ancestor.

### What I Learned

- Leveraging BST properties for efficient searching
- Finding the split point between two nodes
- Iterative traversal on Binary Search Trees
- Reducing unnecessary traversal using node ordering

### Difficulty Faced

Understanding that the Lowest Common Ancestor is the first node where the search paths to both target nodes separate.

### Complexity

- **Time Complexity:** O(h)
- **Space Complexity:** O(1)

---

### 2. LeetCode 236 - Lowest Common Ancestor of a Binary Tree

**Topic:** Binary Tree, Depth-First Search (DFS), Recursion

### Approach

Traverse the tree recursively. If the current node matches either target node, return it. Recursively search both subtrees. If both left and right recursive calls return non-null values, the current node is the Lowest Common Ancestor. Otherwise, return whichever subtree contains a target node.

### What I Learned

- Recursive DFS on Binary Trees
- Combining results from left and right subtrees
- Difference between BST and Binary Tree solutions
- Returning ancestor nodes through recursion

### Difficulty Faced

Visualizing how recursive calls return information upward until the correct Lowest Common Ancestor is identified.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems highlighted how the same objective can have very different solutions depending on the underlying data structure. The BST solution efficiently uses the ordering property to narrow the search path, while the Binary Tree solution relies on recursive DFS to explore both subtrees. Comparing these two approaches reinforced the importance of understanding data structure properties before designing an algorithm.

## Status

✅ Both problems accepted on LeetCode.

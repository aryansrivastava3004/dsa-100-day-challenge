# Day 92 - Merge Two Binary Trees & Binary Tree Pruning

## Problems

### 1. LeetCode 617 - Merge Two Binary Trees

**Topic:** Binary Trees, Recursion, Tree Traversal

### Approach

Traverse both trees simultaneously.

If one node is missing, return the node from the other tree.

When both nodes exist, add their values and recursively merge their left and right subtrees.

### What I Learned

- Traversing two trees simultaneously
- Combining corresponding nodes
- Using recursion for tree transformation
- Handling missing nodes during recursive traversal

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 814 - Binary Tree Pruning

**Topic:** Binary Trees, DFS, Recursion, Postorder Traversal

### Approach

Recursively process the left and right subtrees first.

After processing the children, if the current node is `0` and has no children, it can be safely removed.

This follows a postorder pattern:

Left → Right → Root

### What I Learned

- Using postorder recursion
- Modifying a tree recursively
- Making decisions based on information from child subtrees
- Removing unnecessary nodes from a binary tree

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Overall Learning

Today's problems demonstrated how recursion can be used to transform and simplify binary trees.

In Merge Two Binary Trees, recursive calls combine corresponding nodes from two trees. In Binary Tree Pruning, the same bottom-up approach allows us to determine whether a node should remain after its subtrees have been processed.

The biggest takeaway was understanding how **postorder recursion lets information flow from the children back to the parent**, making it especially useful for tree transformation problems.

## Status

✅ Both problems accepted on LeetCode.

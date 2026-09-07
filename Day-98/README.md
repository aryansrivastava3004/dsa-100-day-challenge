# Day 98 — Binary Trees & BST

## Problems

1. Convert BST to Greater Tree
2. Distribute Coins in Binary Tree

## Topic

Binary Trees, Binary Search Trees, DFS, Postorder Traversal

## Approach

### Convert BST to Greater Tree
Used reverse inorder traversal (Right → Root → Left).
Since a BST gives values in descending order with reverse inorder,
a running sum can be used to update each node.

### Distribute Coins in Binary Tree
Used postorder DFS to calculate the balance of each subtree.
The balance represents extra coins or the number of coins needed.
The absolute balance contributes to the number of moves.

## What I Learned

- Reverse inorder traversal is useful for processing BST nodes
  from largest to smallest.
- A running sum can efficiently transform a BST.
- Postorder traversal helps when a node depends on information
  from its children.
- Subtree balance can be used to calculate tree operations.

## Difficulty Faced

Understanding how traversal order affects the solution and
how subtree balance represents coin movement.

## Complexity

### Convert BST to Greater Tree
- Time: O(n)
- Space: O(h)

### Distribute Coins in Binary Tree
- Time: O(n)
- Space: O(h)

## Overall Learning

Day 98 strengthened my understanding of DFS, tree traversal
orders, BST properties, and subtree-based problem solving.

## Status

✅ Completed

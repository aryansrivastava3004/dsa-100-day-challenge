# Day 83 - Convert Sorted List to Binary Search Tree & Delete Node in a BST

## Problems

### 1. LeetCode 109 - Convert Sorted List to Binary Search Tree

**Topic:** Linked List, Binary Search Tree, Recursion, Two Pointers

### Approach

Use the Slow and Fast pointer technique to find the middle node of the sorted linked list.

The middle element becomes the root of the BST. The left half of the list forms the left subtree, while the right half forms the right subtree.

Repeat the process recursively to construct a height-balanced BST.

### What I Learned

- Finding the middle of a linked list using two pointers
- Building a balanced BST recursively
- Understanding the relationship between sorted data and BST structure
- Using recursion to divide a problem into smaller subproblems

### Complexity

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(log n)

---

### 2. LeetCode 450 - Delete Node in a BST

**Topic:** Binary Search Tree, Recursion

### Approach

Use the BST property to search for the node efficiently.

There are three cases when the target node is found:

1. **No left child:** Replace it with the right child.
2. **No right child:** Replace it with the left child.
3. **Two children:** Find the inorder successor from the right subtree, replace the node's value, and then delete the successor.

### What I Learned

- Searching efficiently in a BST
- Handling different deletion cases
- Finding the inorder successor
- Maintaining BST properties after deletion
- Applying recursion to tree operations

### Complexity

- **Average Time Complexity:** O(log n)
- **Worst Time Complexity:** O(n)
- **Space Complexity:** O(h)

> `h` = height of the tree

---

## Overall Learning

Today's problems marked the beginning of my journey into **Binary Search Trees**.

The first problem showed how a sorted data structure can naturally be converted into a balanced BST, while the second demonstrated how the BST ordering property makes searching and deletion structured and efficient.

The biggest takeaway was understanding that the **BST property is what makes tree operations powerful**.

## Status

✅ Both problems accepted on LeetCode.

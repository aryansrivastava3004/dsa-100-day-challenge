# Day 53 - Minimum Absolute Difference in BST & Find Mode in Binary Search Tree

## Problems

### 1. LeetCode 530 - Minimum Absolute Difference in BST

**Topic:** Binary Search Tree (BST), Inorder Traversal, Recursion

### Approach

Perform an inorder traversal of the BST, which visits nodes in ascending order. Keep track of the previously visited node and calculate the difference between the current and previous values. Update the minimum difference whenever a smaller value is found.

### What I Learned

- Inorder traversal produces sorted values in a BST
- Comparing adjacent values is enough to find the minimum difference
- Maintaining state across recursive calls
- Using BST properties to simplify calculations

### Difficulty Faced

Understanding why only consecutive nodes in the inorder traversal need to be compared instead of checking every possible pair.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

### 2. LeetCode 501 - Find Mode in Binary Search Tree

**Topic:** Binary Tree, DFS, Hash Map

### Approach

Traverse the tree using DFS while counting the frequency of each node value in a dictionary. After the traversal, determine the maximum frequency and return all values that occur that many times.

### What I Learned

- Counting frequencies with a hash map
- Combining DFS with dictionaries
- Handling multiple modes
- Tree traversal independent of node ordering

### Difficulty Faced

Making sure all values with the highest frequency are included in the final result rather than returning only one mode.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Overall Learning

Today's problems reinforced the importance of traversal strategies in Binary Search Trees. I learned how inorder traversal naturally provides sorted values, making problems like finding the minimum absolute difference much simpler. I also practiced combining DFS with hash maps to solve frequency-based tree problems, further strengthening my understanding of recursive tree algorithms.

## Status

✅ Both problems accepted on LeetCode.

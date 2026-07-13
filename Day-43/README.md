# Day 43 - Same Tree & Maximum Depth of Binary Tree

## Problems

### 1. LeetCode 100 - Same Tree

**Topic:** Binary Tree, Recursion

#### Approach

Recursively compare the corresponding nodes of both trees. If both nodes are `None`, they match. If only one is `None` or their values differ, the trees are not identical. Continue checking the left and right subtrees recursively.

#### What I Learned

- Recursive tree traversal
- Comparing two binary trees
- Writing effective recursive base cases
- Traversing left and right subtrees independently

#### Difficulty Faced

Understanding the recursive base cases and why both the left and right subtrees must match for two trees to be considered identical.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(h)

---

### 2. LeetCode 104 - Maximum Depth of Binary Tree

**Topic:** Binary Tree, Recursion

#### Approach

Recursively calculate the depth of the left and right subtrees. The maximum depth of the current node is one plus the greater of the two subtree depths.

#### What I Learned

- Recursive depth calculation
- Divide-and-conquer approach
- Returning values from recursive calls
- Understanding tree height

#### Difficulty Faced

Understanding how recursion computes the depth of each subtree before combining the results to determine the maximum depth.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(h)

---

## Overall Learning

Today marked my introduction to Binary Trees. Unlike linear data structures, trees branch into multiple paths, making recursion the most natural way to solve many tree problems. These problems helped me build a strong foundation by understanding recursive traversal and depth calculation.

## Status

✅ Both problems accepted on LeetCode

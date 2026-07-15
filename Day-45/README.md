# Day 45 - Balanced Binary Tree & Path Sum

## Problems

### 1. LeetCode 110 - Balanced Binary Tree

**Topic:** Binary Tree, Recursion

#### Approach

Recursively calculate the height of the left and right subtrees. If the height difference exceeds one at any node, return `-1` immediately to indicate the tree is unbalanced. Otherwise, return the height of the current subtree.

#### What I Learned

- Efficient height calculation using recursion
- Detecting balanced trees during traversal
- Early termination to optimize recursion
- Combining validation and height calculation into one recursive function

#### Difficulty Faced

Understanding how returning `-1` immediately avoids unnecessary recursive calls once an unbalanced subtree is detected.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(h)

---

### 2. LeetCode 112 - Path Sum

**Topic:** Binary Tree, Recursion

#### Approach

Traverse the tree recursively while subtracting the current node's value from the target sum. When a leaf node is reached, check whether the remaining target equals the leaf's value. If yes, a valid root-to-leaf path exists.

#### What I Learned

- Root-to-leaf traversal
- Passing values through recursive calls
- Identifying leaf nodes
- Recursive state management

#### Difficulty Faced

Understanding that the target sum should only be verified when reaching a leaf node, not during intermediate recursive calls.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(h)

---

## Overall Learning

Today's problems strengthened my understanding of recursive tree traversal. I learned how recursion can be used not only to calculate properties like tree height but also to carry information, such as a remaining target sum, while exploring different root-to-leaf paths. These problems reinforced that recursion is one of the most effective ways to solve Binary Tree problems.

## Status

✅ Both problems accepted on LeetCode

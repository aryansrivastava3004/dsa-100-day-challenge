# Day 44 - Combination Sum III & Symmetric Tree

## Problems

### 1. LeetCode 216 - Combination Sum III

**Topic:** Backtracking

#### Approach

Use backtracking to generate all possible combinations of numbers from 1 to 9. Keep adding numbers to the current combination until it contains exactly `k` numbers. If the sum equals `n`, store the combination. After each recursive call, remove the last number to explore other possibilities.

#### What I Learned

- Introduction to Backtracking
- Recursive decision making
- Generating valid combinations
- Undoing choices using backtracking

#### Difficulty Faced

Understanding why the last selected number must be removed after each recursive call so that other combinations can be explored correctly.

#### Complexity

Time Complexity: O(C(9, k))

Space Complexity: O(k)

---

### 2. LeetCode 101 - Symmetric Tree

**Topic:** Binary Tree, Recursion

#### Approach

Compare the left and right subtrees recursively. Two trees are mirrors if:
- Their root values are equal.
- The left subtree of one matches the right subtree of the other.
- The right subtree of one matches the left subtree of the other.

#### What I Learned

- Mirror recursion
- Comparing opposite branches
- Recursive tree traversal
- Binary tree symmetry checking

#### Difficulty Faced

Understanding why opposite branches must be compared instead of corresponding branches to determine symmetry.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(h)

---

## Overall Learning

Today's problems introduced me to Backtracking while also strengthening my understanding of recursion in Binary Trees. Although both solutions use recursion, they solve problems in different ways—Backtracking explores multiple possible choices, whereas tree recursion naturally traverses different branches. It was interesting to see how the same concept of recursion can be applied in completely different contexts.

## Status

✅ Both problems accepted on LeetCode

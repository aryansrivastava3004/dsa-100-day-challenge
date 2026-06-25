# Day 25 - Binary Search & Search Insert Position

## Problems

### 1. LeetCode 704 - Binary Search

**Topic:** Arrays, Binary Search

#### Approach

Use two pointers (`left` and `right`) to repeatedly divide the search space in half. Compare the middle element with the target and adjust the search range accordingly until the target is found or the search space becomes empty.

#### What I Learned

- Binary Search algorithm
- Dividing the search space efficiently
- Using left, right, and mid pointers
- Searching in sorted arrays in logarithmic time

#### Difficulty Faced

Understanding when to move the left pointer versus the right pointer based on the comparison with the middle element.

#### Complexity

Time Complexity: O(log n)

Space Complexity: O(1)

---

### 2. LeetCode 35 - Search Insert Position

**Topic:** Arrays, Binary Search

#### Approach

Apply Binary Search to locate the target. If the target is not found, return the `left` pointer, which represents the correct insertion position after the search ends.

#### What I Learned

- Applying Binary Search to different problems
- Finding insertion positions efficiently
- Reusing the same algorithm with slight modifications
- Understanding why `left` becomes the insertion index

#### Difficulty Faced

Understanding why the `left` pointer represents the correct insertion position when the target does not exist in the array.

#### Complexity

Time Complexity: O(log n)

Space Complexity: O(1)

---

## Overall Learning

Today marked my introduction to Binary Search. I learned how reducing the search space by half makes searching extremely efficient and how the same algorithm can be adapted to solve different types of problems with only minor changes.

## Status

✅ Both problems accepted on LeetCode

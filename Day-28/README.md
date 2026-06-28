# Day 28 - Find Minimum in Rotated Sorted Array & Fibonacci Number

## Problems

### 1. LeetCode 153 - Find Minimum in Rotated Sorted Array

**Topic:** Binary Search

#### Approach

Use Binary Search to compare the middle element with the rightmost element. If the middle element is greater, the minimum lies in the right half; otherwise, it lies in the left half (including the middle element). Continue until both pointers meet.

#### What I Learned

- Binary Search on rotated arrays
- Finding the minimum element efficiently
- Eliminating half of the search space
- Comparing with the rightmost element

#### Difficulty Faced

Understanding why comparing `nums[mid]` with `nums[right]` reveals which half contains the minimum element.

#### Complexity

Time Complexity: O(log n)

Space Complexity: O(1)

---

### 2. LeetCode 509 - Fibonacci Number

**Topic:** Dynamic Programming

#### Approach

Use an iterative approach to calculate Fibonacci numbers by storing only the previous two values. This avoids recursion and reduces space usage while maintaining efficiency.

#### What I Learned

- Dynamic Programming basics
- Iterative computation
- Optimizing space usage
- Building answers from previous results

#### Difficulty Faced

Understanding how storing only the previous two Fibonacci numbers is sufficient instead of maintaining the entire sequence.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems introduced two different problem-solving techniques. I strengthened my Binary Search skills by solving another rotated array problem and took my first step into Dynamic Programming by learning how previous results can be reused to build efficient solutions.

## Status

✅ Both problems accepted on LeetCode

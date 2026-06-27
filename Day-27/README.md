# Day 27 - First Bad Version & Search in Rotated Sorted Array

## Problems

### 1. LeetCode 278 - First Bad Version

**Topic:** Binary Search

#### Approach

Use Binary Search to locate the first bad version. If the current version is bad, continue searching in the left half (including the current version). Otherwise, search in the right half. Continue until both pointers meet.

#### What I Learned

- Binary Search on answer space
- Finding the first valid occurrence
- Lower-bound Binary Search
- Efficiently narrowing the search range

#### Difficulty Faced

Understanding why `right = mid` is used instead of `right = mid - 1` when searching for the first valid answer.

#### Complexity

Time Complexity: O(log n)

Space Complexity: O(1)

---

### 2. LeetCode 33 - Search in Rotated Sorted Array

**Topic:** Binary Search

#### Approach

At each step, identify which half of the array is sorted. Check whether the target lies within that sorted half and discard the other half. Repeat until the target is found or the search space becomes empty.

#### What I Learned

- Binary Search on rotated arrays
- Identifying the sorted half
- Narrowing the search intelligently
- Applying Binary Search beyond simple sorted arrays

#### Difficulty Faced

Understanding how to determine which half of the array is sorted and deciding where the target can exist.

#### Complexity

Time Complexity: O(log n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems introduced more advanced Binary Search patterns. I learned how the same algorithm can be adapted to solve different types of search problems, from finding the first valid answer to searching efficiently in rotated sorted arrays.

## Status

✅ Both problems accepted on LeetCode

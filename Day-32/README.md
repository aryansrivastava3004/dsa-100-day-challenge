# Day 32 - Squares of a Sorted Array & Sort Colors

## Problems

### 1. LeetCode 977 - Squares of a Sorted Array

**Topic:** Arrays, Two Pointers

#### Approach

Use two pointers at the beginning and end of the sorted array. Compare the absolute values, place the larger square at the end of a new array, and move the corresponding pointer inward until all positions are filled.

#### What I Learned

- Two-pointer technique
- Comparing absolute values
- Filling an array from the end
- Optimizing beyond simply sorting again

#### Difficulty Faced

Understanding why comparing absolute values from both ends correctly identifies the largest square at each step.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(n)

---

### 2. LeetCode 75 - Sort Colors

**Topic:** Arrays, Sorting, Three Pointers

#### Approach

Use the Dutch National Flag Algorithm with three pointers (`low`, `mid`, and `high`). Partition the array into three sections by moving 0s to the beginning, 2s to the end, and leaving 1s in the middle.

#### What I Learned

- Dutch National Flag Algorithm
- Three-pointer technique
- In-place sorting
- Efficient array partitioning

#### Difficulty Faced

Understanding why the `mid` pointer should not be incremented immediately after swapping with the `high` pointer, since the swapped element still needs to be processed.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems reinforced efficient array manipulation techniques. I learned how the Two Pointers approach can transform sorted data efficiently and how the Dutch National Flag Algorithm performs in-place sorting in linear time without requiring extra memory.

## Status

✅ Both problems accepted on LeetCode

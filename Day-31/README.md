# Day 31 - Sort an Array & Merge Sorted Array

## Problems

### 1. LeetCode 912 - Sort an Array

**Topic:** Sorting, Divide and Conquer

#### Approach

Implemented Merge Sort by recursively dividing the array into two halves until each subarray contained a single element. Then merged the sorted halves back together to obtain the final sorted array.

#### What I Learned

- Merge Sort algorithm
- Divide and Conquer strategy
- Recursive problem solving
- Merging two sorted arrays efficiently

#### Difficulty Faced

Understanding how recursively dividing the array and merging the sorted halves results in a completely sorted array.

#### Complexity

Time Complexity: O(n log n)

Space Complexity: O(n)

---

### 2. LeetCode 88 - Merge Sorted Array

**Topic:** Arrays, Two Pointers

#### Approach

Use three pointers starting from the end of both arrays. Compare the largest remaining elements and place them at the end of `nums1`. This avoids overwriting values that have not yet been processed.

#### What I Learned

- Two-pointer technique
- In-place array merging
- Working backwards efficiently
- Space optimization

#### Difficulty Faced

Understanding why filling the array from the end prevents overwriting useful elements.

#### Complexity

Time Complexity: O(m + n)

Space Complexity: O(1)

---

## Overall Learning

Today marked my introduction to sorting algorithms through Merge Sort. I also reinforced my understanding of the two-pointer technique by solving an in-place array merging problem. These problems highlighted the importance of choosing the right algorithm based on the problem's constraints.

## Status

✅ Both problems accepted on LeetCode

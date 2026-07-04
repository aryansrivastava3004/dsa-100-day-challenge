# Day 33 - Merge Intervals & Insert Interval

## Problems

### 1. LeetCode 56 - Merge Intervals

**Topic:** Arrays, Sorting, Intervals

#### Approach

Sort the intervals by their starting values. Traverse the sorted list and merge overlapping intervals by updating the ending point of the previous interval whenever an overlap is found.

#### What I Learned

- Sorting intervals before processing
- Detecting overlapping intervals
- Merging ranges efficiently
- Working with nested lists

#### Difficulty Faced

Understanding why sorting by the starting value makes merging intervals straightforward.

#### Complexity

Time Complexity: O(n log n)

Space Complexity: O(n)

---

### 2. LeetCode 57 - Insert Interval

**Topic:** Arrays, Intervals

#### Approach

Process the intervals in three stages:
1. Add all intervals before the new interval.
2. Merge all overlapping intervals with the new interval.
3. Add the remaining intervals.

#### What I Learned

- Inserting while maintaining sorted order
- Interval merging techniques
- Processing data in logical phases
- Managing overlapping ranges

#### Difficulty Faced

Breaking the solution into three separate phases made the implementation much easier to understand.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(n)

---

## Overall Learning

Today's problems introduced interval-based questions, where sorting and careful traversal are key. I learned how organizing data first often leads to much simpler solutions.

## Status

✅ Both problems accepted on LeetCode

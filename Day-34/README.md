# Day 34 - Middle of the Linked List & Linked List Cycle

## Problems

### 1. LeetCode 876 - Middle of the Linked List

**Topic:** Linked List, Fast & Slow Pointers

#### Approach

Use two pointers starting at the head. Move the slow pointer one step and the fast pointer two steps at a time. When the fast pointer reaches the end, the slow pointer will be at the middle.

#### What I Learned

- Fast & Slow Pointer technique
- Single-pass traversal
- Efficient linked list processing
- Pointer movement strategies

#### Difficulty Faced

Understanding why moving one pointer twice as fast guarantees the other pointer reaches the middle.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

### 2. LeetCode 141 - Linked List Cycle

**Topic:** Linked List, Floyd's Cycle Detection

#### Approach

Use two pointers moving at different speeds. If a cycle exists, the fast pointer will eventually meet the slow pointer. Otherwise, the fast pointer reaches the end of the list.

#### What I Learned

- Floyd's Cycle Detection Algorithm
- Cycle detection without extra memory
- Fast & Slow Pointer technique
- Efficient linked list traversal

#### Difficulty Faced

Understanding why two pointers moving at different speeds are guaranteed to meet inside a cycle.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Overall Learning

Today marked my introduction to Linked Lists. I learned how the Fast & Slow Pointer technique can solve multiple problems efficiently without using extra space, making it one of the most valuable patterns in linked list problems.

## Status

✅ Both problems accepted on LeetCode

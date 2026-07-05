# Day 35 - Merge Two Sorted Lists & Palindrome Linked List

## Problems

### 1. LeetCode 21 - Merge Two Sorted Lists

**Topic:** Linked List

#### Approach

Create a dummy node to simplify list construction. Compare the current nodes of both linked lists and attach the smaller one to the result list. Continue until one list is exhausted, then attach the remaining nodes of the other list.

#### What I Learned

- Using a dummy node to simplify linked list operations
- Merging two sorted linked lists efficiently
- Pointer manipulation
- Building linked lists without extra memory

#### Difficulty Faced

Understanding how the dummy node removes the need for special handling of the head node.

#### Complexity

Time Complexity: O(n + m)

Space Complexity: O(1)

---

### 2. LeetCode 234 - Palindrome Linked List

**Topic:** Linked List, Fast & Slow Pointers

#### Approach

Use the Fast & Slow Pointer technique to find the middle of the linked list. Reverse the second half in-place and compare both halves node by node to determine whether the list is a palindrome.

#### What I Learned

- Fast & Slow Pointer technique
- Reversing a linked list
- Comparing linked lists efficiently
- Solving problems without extra space

#### Difficulty Faced

Understanding how reversing only the second half allows an efficient palindrome check while maintaining O(1) extra space.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems strengthened my understanding of linked lists by introducing two essential interview techniques: using a dummy node for cleaner list construction and combining multiple pointer-based approaches to solve more complex problems efficiently.

## Status

✅ Both problems accepted on LeetCode

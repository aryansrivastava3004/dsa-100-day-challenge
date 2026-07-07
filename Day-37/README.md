# Day 37 - Delete Node in a Linked List & Linked List Cycle II

## Problems

### 1. LeetCode 237 - Delete Node in a Linked List

**Topic:** Linked List

#### Approach

Since the head of the linked list is not available, copy the value of the next node into the current node and then bypass the next node by updating the pointer. This effectively removes the target node from the list.

#### What I Learned

- Deleting a node without access to the head
- Updating node values and pointers
- Solving linked list problems with limited information
- Understanding why direct deletion isn't possible

#### Difficulty Faced

Understanding why copying the next node's value is necessary instead of deleting the current node directly.

#### Complexity

Time Complexity: O(1)

Space Complexity: O(1)

---

### 2. LeetCode 142 - Linked List Cycle II

**Topic:** Linked List, Fast & Slow Pointers

#### Approach

Use Floyd's Cycle Detection Algorithm to detect whether a cycle exists. Once the slow and fast pointers meet, reset the slow pointer to the head. Move both pointers one step at a time until they meet again—the meeting point is the start of the cycle.

#### What I Learned

- Floyd's Cycle Detection Algorithm
- Finding the starting node of a cycle
- Mathematical reasoning behind pointer movement
- Solving cycle problems without extra memory

#### Difficulty Faced

Understanding why resetting one pointer to the head causes both pointers to meet exactly at the beginning of the cycle.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems strengthened my understanding of advanced linked list techniques. I learned that efficient pointer manipulation can solve problems that initially seem impossible, such as deleting a node without the head reference and locating the exact starting point of a cycle.

## Status

✅ Both problems accepted on LeetCode

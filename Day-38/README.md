# Day 38 - Odd Even Linked List & Swap Nodes in Pairs

## Problems

### 1. LeetCode 328 - Odd Even Linked List

**Topic:** Linked List

#### Approach

Separate the linked list into two lists—one containing nodes at odd positions and the other containing nodes at even positions. Traverse both lists simultaneously while updating pointers, then connect the odd list to the head of the even list.

#### What I Learned

- Rearranging linked lists in-place
- Maintaining separate odd and even node sequences
- Reconnecting linked list segments
- Careful pointer manipulation

#### Difficulty Faced

Understanding how to update the odd and even pointers without breaking the original linked list.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

### 2. LeetCode 24 - Swap Nodes in Pairs

**Topic:** Linked List

#### Approach

Use a dummy node before the head to simplify swapping. Process the linked list two nodes at a time by updating pointers in the correct order without changing node values.

#### What I Learned

- Swapping nodes without modifying values
- Effective use of a dummy node
- Pointer manipulation for node reordering
- Handling edge cases in linked lists

#### Difficulty Faced

Understanding the correct sequence of pointer updates so that no nodes are lost during swapping.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems focused on rearranging nodes within a linked list. I learned that careful pointer management allows complex modifications to be performed efficiently without using additional memory or changing node values.

## Status

✅ Both problems accepted on LeetCode

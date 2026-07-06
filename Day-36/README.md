# Day 36 - Remove Linked List Elements & Intersection of Two Linked Lists

## Problems

### 1. LeetCode 203 - Remove Linked List Elements

**Topic:** Linked List

#### Approach

Create a dummy node before the head of the list. Traverse the linked list while checking the next node. If the next node contains the target value, skip it by updating the pointer; otherwise, move to the next node.

#### What I Learned

- Using a dummy node for safe node deletion
- Removing nodes without breaking the linked list
- Handling deletion of the head node
- Pointer manipulation in linked lists

#### Difficulty Faced

Understanding why introducing a dummy node simplifies edge cases, especially when the head node itself needs to be removed.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

### 2. LeetCode 160 - Intersection of Two Linked Lists

**Topic:** Linked List, Two Pointers

#### Approach

Use two pointers, one for each linked list. When a pointer reaches the end of its list, redirect it to the head of the other list. Both pointers eventually travel the same total distance and meet at the intersection node (or both become `None` if no intersection exists).

#### What I Learned

- Two-pointer technique on linked lists
- Pointer switching strategy
- Finding intersections without extra memory
- Equalizing traversal distance

#### Difficulty Faced

Understanding how switching pointers allows both pointers to traverse equal distances, ensuring they meet at the intersection node if one exists.

#### Complexity

Time Complexity: O(n + m)

Space Complexity: O(1)

---

## Overall Learning

Today's problems strengthened my understanding of linked list manipulation. I learned how dummy nodes simplify deletion problems and how a clever two-pointer strategy can find the intersection of two linked lists without using additional memory.

## Status

✅ Both problems accepted on LeetCode

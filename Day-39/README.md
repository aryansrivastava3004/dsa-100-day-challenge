# Day 39 - Min Stack & Valid Parentheses

## Problems

### 1. LeetCode 155 - Min Stack

**Topic:** Stack, Design

#### Approach

Maintain two stacks:
- One stores all the elements.
- The other stores the minimum element at every stage.

Whenever a new element is pushed, compare it with the current minimum and update the minimum stack if necessary. While popping, remove the top element from the minimum stack only if it matches the popped value.

#### What I Learned

- Stack data structure
- Designing custom data structures
- Maintaining an auxiliary stack
- Retrieving the minimum element in constant time

#### Difficulty Faced

Understanding why maintaining a separate stack for minimum values allows `getMin()` to execute in **O(1)** time instead of searching the entire stack.

#### Complexity

Time Complexity:

- Push → O(1)
- Pop → O(1)
- Top → O(1)
- GetMin → O(1)

Space Complexity: O(n)

---

### 2. LeetCode 20 - Valid Parentheses

**Topic:** Stack

#### Approach

Traverse the string character by character. Push every opening bracket onto the stack. When a closing bracket is encountered, check whether it matches the most recent opening bracket. If all brackets match correctly and the stack is empty at the end, the string is valid.

#### What I Learned

- LIFO (Last In, First Out) principle
- Stack implementation
- Matching opening and closing brackets
- Using dictionaries for cleaner code

#### Difficulty Faced

Understanding why the most recently opened bracket must always be closed first, making a stack the ideal data structure for this problem.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(n)

---

## Overall Learning

Today marked my introduction to stacks. I learned how this fundamental data structure can solve different types of problems, from designing efficient systems like Min Stack to validating balanced expressions using the LIFO principle.

## Status

✅ Both problems accepted on LeetCode

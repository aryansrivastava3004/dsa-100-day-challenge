# Day 42 - Backspace String Compare & Next Greater Element I

## Problems

### 1. LeetCode 844 - Backspace String Compare

**Topic:** Stack, Strings

#### Approach

Use a stack to simulate typing each string. Push normal characters onto the stack and remove the top element whenever a backspace (`#`) is encountered. After processing both strings, compare the resulting stacks.

#### What I Learned

- Stack-based string processing
- Simulating backspace operations
- Using helper functions for cleaner code
- Comparing processed strings efficiently

#### Difficulty Faced

Understanding how a stack naturally simulates typing and deleting characters, making backspace operations simple to implement.

#### Complexity

Time Complexity: O(n + m)

Space Complexity: O(n + m)

---

### 2. LeetCode 496 - Next Greater Element I

**Topic:** Stack, Monotonic Stack

#### Approach

Traverse `nums2` while maintaining a **monotonic decreasing stack**. Whenever a larger element is found, assign it as the next greater element for all smaller elements at the top of the stack. Store the results in a hash map and use it to answer queries for `nums1`.

#### What I Learned

- Monotonic Stack pattern
- Finding the next greater element efficiently
- Combining stacks with hash maps
- Optimizing brute-force comparisons

#### Difficulty Faced

Understanding why maintaining a decreasing stack guarantees that the first larger element encountered is the correct next greater element.

#### Complexity

Time Complexity: O(n + m)

Space Complexity: O(n)

---

## Overall Learning

Today's problems strengthened my understanding of stack applications. I learned how stacks can simplify string processing problems and how the Monotonic Stack pattern efficiently solves "next greater element" type questions that would otherwise require nested loops.

## Status

✅ Both problems accepted on LeetCode

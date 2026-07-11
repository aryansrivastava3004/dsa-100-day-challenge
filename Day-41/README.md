# Day 41 - Daily Temperatures & Baseball Game

## Problems

### 1. LeetCode 739 - Daily Temperatures

**Topic:** Stack, Monotonic Stack

#### Approach

Traverse the temperature array while maintaining a **monotonic decreasing stack** of indices. Whenever a warmer temperature is found, pop previous indices from the stack and calculate how many days they had to wait.

#### What I Learned

- Monotonic Stack pattern
- Storing indices instead of values
- Finding the next greater element efficiently
- Solving array problems in linear time

#### Difficulty Faced

Understanding why storing indices instead of temperatures makes it easy to calculate the waiting period for each day.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(n)

---

### 2. LeetCode 682 - Baseball Game

**Topic:** Stack

#### Approach

Use a stack to maintain valid scores. Perform operations according to the given rules:
- Push new scores.
- Remove the previous score.
- Double the previous score.
- Add the previous two scores.

Finally, return the sum of all valid scores.

#### What I Learned

- Stack-based simulation
- Maintaining previous results
- Implementing multiple stack operations
- Using stacks for state management

#### Difficulty Faced

Understanding how the stack naturally keeps track of the valid record after each operation, making additions and deletions straightforward.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(n)

---

## Overall Learning

Today's problems introduced the **Monotonic Stack**, an important interview pattern for solving "next greater element" type questions efficiently. I also reinforced my understanding of stacks through a simulation problem, showing how the same data structure can solve different categories of problems.

## Status

✅ Both problems accepted on LeetCode

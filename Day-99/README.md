# Day 99 — Dynamic Programming

## Problems

1. House Robber
2. House Robber II

## Topic

Dynamic Programming, Arrays

## Approach

### House Robber
At each house, choose between robbing the current house
and skipping it. The current maximum depends on the previous
two states.

### House Robber II
Since the houses are arranged in a circle, the first and last
houses cannot both be robbed. Solve two linear cases:
- Exclude the last house
- Exclude the first house

Take the maximum of the two results.

## What I Learned

- How to identify states in Dynamic Programming.
- How to optimize DP from O(n) space to O(1) space.
- How circular problems can be divided into simpler cases.
- How to build transitions based on previous states.

## Difficulty Faced

The main challenge was handling the circular arrangement
in House Robber II without selecting both the first and last houses.

## Complexity

### House Robber
- Time: O(n)
- Space: O(1)

### House Robber II
- Time: O(n)
- Space: O(1)

## Overall Learning

Day 99 strengthened my understanding of Dynamic Programming
and showed how careful state selection can make solutions both
simple and space efficient.

## Status

✅ Completed

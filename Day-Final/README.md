# Day 100 — Dynamic Programming

## Problems

1. Longest Increasing Subsequence
2. Coin Change

## Topic

Dynamic Programming, Arrays

## Approach

### Longest Increasing Subsequence

Used Dynamic Programming where dp[i] represents the length
of the longest increasing subsequence ending at index i.

For every previous element, if it is smaller than the current
element, the current subsequence can be extended.

### Coin Change

Used bottom-up Dynamic Programming.

dp[i] stores the minimum number of coins required to make
amount i. For every amount, each available coin is checked
and the minimum valid result is stored.

## What I Learned

- How to define DP states and transitions.
- How smaller subproblems can be used to solve larger problems.
- How to solve optimization problems using Dynamic Programming.
- How to handle impossible states efficiently.

## Difficulty Faced

The main challenge was identifying the correct DP state
and transition for both problems.

## Complexity

### Longest Increasing Subsequence
- Time: O(n²)
- Space: O(n)

### Coin Change
- Time: O(amount × number of coins)
- Space: O(amount)

## Overall Learning

Day 100 completed my 100 Days of Coding Challenge.
This journey strengthened my DSA, Python, problem-solving,
and consistency skills.

## Status

✅ Challenge Completed

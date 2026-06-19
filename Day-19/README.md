# Day 19 - Happy Number

## Problem

LeetCode 202 - Happy Number

## Topic

Hashing, Math

## Approach

Use a set to store all previously seen numbers. Repeatedly replace the number with the sum of the squares of its digits. If the number becomes 1, it is a happy number. If a number repeats, a cycle has been detected, so it is not a happy number.

## What I Learned

- Detecting cycles using a set
- Breaking a number into individual digits
- Using modulo (%) and integer division (//)
- Applying hashing beyond arrays and strings

## Difficulty Faced

Understanding why a set is needed to detect repeated numbers and prevent the algorithm from entering an infinite loop.

## Complexity

Time Complexity: O(log n)

Space Complexity: O(log n)

## Status

✅ Accepted on LeetCode

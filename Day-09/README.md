# Day 9 - Single Number

## Problem

LeetCode 136 - Single Number

## Approach

Use the XOR operator to find the element that appears only once. Since a ^ a = 0 and a ^ 0 = a, all duplicate numbers cancel out, leaving only the unique number.

## What I Learned

- Introduction to bit manipulation
- Understanding XOR operations
- How duplicate values cancel each other out
- Solving problems with O(1) extra space

## Difficulty Faced

Understanding why XOR cancels duplicate values and how it can be used to find the unique element efficiently.

## Complexity

Time Complexity: O(n)

Space Complexity: O(1)

## Status

✅ Accepted on LeetCode

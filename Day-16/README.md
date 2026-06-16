# Day 16 - First Unique Character in a String

## Problem

LeetCode 387 - First Unique Character in a String

## Topic

Strings, Hashing

## Approach

First count the frequency of each character using a dictionary. Then traverse the string again and return the index of the first character whose frequency is 1.

## What I Learned

- Character frequency counting
- Using hash maps with strings
- Multi-pass problem solving
- Finding unique elements efficiently

## Difficulty Faced

Understanding why we need a second traversal after counting frequencies instead of returning immediately during the first pass.

## Complexity

Time Complexity: O(n)

Space Complexity: O(1)

## Status

✅ Accepted on LeetCode

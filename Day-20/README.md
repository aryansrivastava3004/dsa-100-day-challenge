# Day 20 - Isomorphic Strings

## Problem

LeetCode 205 - Isomorphic Strings

## Topic

Strings, Hashing

## Approach

Use two hash maps to maintain a one-to-one mapping between the characters of both strings. One dictionary maps characters from the first string to the second, while the other verifies the reverse mapping. If either mapping becomes inconsistent, the strings are not isomorphic.

## What I Learned

- Creating one-to-one character mappings
- Using two hash maps together
- Working with strings and character relationships
- Ensuring bidirectional consistency

## Difficulty Faced

Understanding why one dictionary is not sufficient and why the mapping must be validated in both directions.

## Complexity

Time Complexity: O(n)

Space Complexity: O(n)

## Status

✅ Accepted on LeetCode

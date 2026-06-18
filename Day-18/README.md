# Day 18 - Contains Duplicate II

## Problem

LeetCode 219 - Contains Duplicate II

## Topic

Arrays, Hashing

## Approach

Use a dictionary to store the most recent index of each element. While traversing the array, check if the current element has appeared before and whether the distance between the current index and its previous index is less than or equal to `k`.

## What I Learned

- Using hash maps to store indices
- Calculating distances between duplicate elements
- Solving lookup problems in a single traversal
- Strengthening my understanding of hashing

## Difficulty Faced

Understanding why storing the latest index of each element is sufficient to efficiently determine whether duplicate values are within the required distance.

## Complexity

Time Complexity: O(n)

Space Complexity: O(n)

## Status

✅ Accepted on LeetCode

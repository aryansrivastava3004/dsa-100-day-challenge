# Day 22 - Length of Last Word & Longest Common Prefix

## Problems

### 1. LeetCode 58 - Length of Last Word

**Topic:** Strings

#### Approach

Split the string into words using `split()`, which automatically removes extra spaces. Then return the length of the last word.

#### What I Learned

- String manipulation
- Using `split()` effectively
- Working with lists generated from strings
- Leveraging Python's built-in methods

#### Difficulty Faced

Understanding how `split()` automatically ignores leading, trailing, and multiple spaces between words.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(n)

---

### 2. LeetCode 14 - Longest Common Prefix

**Topic:** Strings

#### Approach

Assume the first string is the common prefix. Compare it with each remaining string and keep shortening the prefix until all strings start with it.

#### What I Learned

- Comparing multiple strings efficiently
- Using `startswith()` in Python
- Reducing the search space step by step
- Finding common patterns among strings

#### Difficulty Faced

Understanding why reducing the prefix gradually guarantees finding the longest common prefix shared by every string.

#### Complexity

Time Complexity: O(n × m)

Space Complexity: O(1)

---

## Overall Learning

Today's problems focused on string manipulation using Python's built-in methods. I learned that understanding functions like `split()` and `startswith()` can lead to simple, clean, and efficient solutions.

## Status

✅ Both problems accepted on LeetCode

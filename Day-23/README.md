# Day 23 - Find the Index of the First Occurrence in a String & Is Subsequence

## Problems

### 1. LeetCode 28 - Find the Index of the First Occurrence in a String

**Topic:** Strings

#### Approach

Traverse the main string and compare each substring of length equal to the target string using slicing. Return the starting index when a match is found.

#### What I Learned

- String slicing
- Searching for substrings
- Basic sliding window concept
- Comparing fixed-length substrings efficiently

#### Difficulty Faced

Understanding how slicing simplifies substring comparison without checking each character individually.

#### Complexity

Time Complexity: O(n × m)

Space Complexity: O(1)

---

### 2. LeetCode 392 - Is Subsequence

**Topic:** Strings, Two Pointers

#### Approach

Use two pointers to traverse both strings. Move both pointers when characters match; otherwise, move only the pointer of the second string until all characters of the first string are found.

#### What I Learned

- Two-pointer traversal
- Sequential character matching
- Traversing two strings simultaneously
- Efficient subsequence checking

#### Difficulty Faced

Understanding why only one pointer moves when characters don't match while both move when they do.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems helped me strengthen my understanding of string manipulation. I learned how different approaches, such as string slicing and the two-pointer technique, can efficiently solve common string-related problems.

## Status

✅ Both problems accepted on LeetCode

# Day 24 - Merge Strings Alternately & Ransom Note

## Problems

### 1. LeetCode 1768 - Merge Strings Alternately

**Topic:** Strings, Two Pointers

#### Approach

Use two pointers to traverse both strings simultaneously. Add characters alternately to a result list and append any remaining characters once one string ends.

#### What I Learned

- Two-pointer technique with strings
- Building strings efficiently using lists
- Handling strings of different lengths
- Using `"".join()` for efficient string creation

#### Difficulty Faced

Understanding how to handle the remaining characters when one string is longer than the other.

#### Complexity

Time Complexity: O(n + m)

Space Complexity: O(n + m)

---

### 2. LeetCode 383 - Ransom Note

**Topic:** Strings, Hashing

#### Approach

Count the frequency of each character in the magazine using a dictionary. Then check if every character required by the ransom note is available in sufficient quantity.

#### What I Learned

- Character frequency counting
- Hash maps with strings
- Resource allocation using frequencies
- Checking availability before usage

#### Difficulty Faced

Understanding how frequency counts decrease as characters are used from the magazine.

#### Complexity

Time Complexity: O(n + m)

Space Complexity: O(1)

---

## Overall Learning

Today's problems showed two different approaches to string-based questions. One relied on the two-pointer technique, while the other used hashing and frequency counting. It reinforced how multiple DSA patterns can be applied to solve different types of string problems efficiently.

## Status

✅ Both problems accepted on LeetCode

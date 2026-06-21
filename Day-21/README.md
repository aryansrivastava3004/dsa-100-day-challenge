# Day 21 - Reverse String & Valid Palindrome

## Problems

### 1. LeetCode 344 - Reverse String

**Topic:** Strings, Two Pointers

#### Approach

Use two pointers starting from both ends of the string. Swap the characters and move the pointers toward the center until they meet.

#### What I Learned

- Two-pointer technique
- In-place swapping
- Working from both ends of an array
- Space optimization

#### Difficulty Faced

Understanding how two pointers can reverse a string without creating another array.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

### 2. LeetCode 125 - Valid Palindrome

**Topic:** Strings, Two Pointers

#### Approach

Use two pointers to compare characters from both ends. Skip non-alphanumeric characters and compare letters after converting them to lowercase.

#### What I Learned

- Two-pointer traversal
- Using `isalnum()` to ignore special characters
- Case-insensitive comparison using `lower()`
- Efficient string validation

#### Difficulty Faced

Understanding how to skip non-alphanumeric characters while keeping both pointers synchronized.

#### Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems strengthened my understanding of the Two Pointers technique. I learned how the same pattern can be applied to different string problems—whether it's reversing a string or validating a palindrome.

## Status

✅ Both problems accepted on LeetCode

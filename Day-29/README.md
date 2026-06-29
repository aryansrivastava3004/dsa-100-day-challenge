# Day 29 - Power of Two & Power of Three

## Problems

### 1. LeetCode 231 - Power of Two

**Topic:** Bit Manipulation, Math

#### Approach

First, check whether the number is positive. Then use the bitwise expression `n & (n - 1)` to determine if the number has exactly one set bit. If the result is zero, the number is a power of two.

#### What I Learned

- Bit manipulation fundamentals
- Using bitwise AND (`&`) in Python
- Identifying powers of two efficiently
- Understanding binary representations of numbers

#### Difficulty Faced

Understanding why `n & (n - 1)` removes the rightmost set bit and why the result becomes zero only for powers of two.

#### Complexity

Time Complexity: O(1)

Space Complexity: O(1)

---

### 2. LeetCode 326 - Power of Three

**Topic:** Math

#### Approach

Repeatedly divide the number by 3 while it remains divisible. If the final value becomes 1, the original number is a power of three.

#### What I Learned

- Mathematical problem solving
- Repeated division technique
- Recognizing powers using loops
- Handling edge cases

#### Difficulty Faced

Understanding why repeatedly dividing by 3 correctly determines whether a number is a power of three.

#### Complexity

Time Complexity: O(log₃ n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems focused on identifying mathematical properties of numbers. I learned that efficient solutions often come from understanding binary representations and mathematical patterns rather than relying on brute-force approaches.

## Status

✅ Both problems accepted on LeetCode

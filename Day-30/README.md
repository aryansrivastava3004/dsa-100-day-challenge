# Day 30 - Power of Four & Pow(x, n)

## Problems

### 1. LeetCode 342 - Power of Four

**Topic:** Math

#### Approach

Repeatedly divide the number by 4 while it remains divisible. If the final value becomes 1, the number is a power of four; otherwise, it is not.

#### What I Learned

- Identifying powers using repeated division
- Recognizing mathematical patterns
- Handling edge cases for non-positive numbers
- Extending power-checking logic to different bases

#### Difficulty Faced

Understanding why repeatedly dividing by 4 correctly determines whether a number is a power of four.

#### Complexity

Time Complexity: O(log₄ n)

Space Complexity: O(1)

---

### 2. LeetCode 50 - Pow(x, n)

**Topic:** Math, Binary Exponentiation

#### Approach

Use Binary Exponentiation (Fast Exponentiation) by repeatedly squaring the base and halving the exponent. Multiply the result whenever the exponent is odd. Handle negative exponents by inverting the base.

#### What I Learned

- Fast (Binary) Exponentiation
- Optimizing from O(n) to O(log n)
- Handling negative exponents
- Reusing previously computed values efficiently

#### Difficulty Faced

Understanding how repeated squaring reduces the number of multiplications while still producing the correct result.

#### Complexity

Time Complexity: O(log n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems strengthened my mathematical problem-solving skills. I learned that understanding mathematical properties and optimization techniques can significantly improve the efficiency of solutions. Binary Exponentiation, in particular, showed how a simple change in approach can reduce the time complexity from linear to logarithmic.

## Status

✅ Both problems accepted on LeetCode

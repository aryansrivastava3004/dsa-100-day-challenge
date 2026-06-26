# Day 26 - Sqrt(x) & Valid Perfect Square

## Problems

### 1. LeetCode 69 - Sqrt(x)

**Topic:** Binary Search

#### Approach

Apply Binary Search on the range from 1 to x. Compare the square of the middle value with x and adjust the search range until the integer square root is found.

#### What I Learned

- Applying Binary Search to mathematical problems
- Finding the floor value of a square root
- Searching over a range of possible answers
- Returning the closest valid result

#### Difficulty Faced

Understanding why the `right` pointer represents the integer square root after the Binary Search ends.

#### Complexity

Time Complexity: O(log n)

Space Complexity: O(1)

---

### 2. LeetCode 367 - Valid Perfect Square

**Topic:** Binary Search

#### Approach

Use Binary Search on the range from 1 to num. Calculate the square of the middle value and compare it with the target number until a perfect square is found or the search space is exhausted.

#### What I Learned

- Binary Search for mathematical validation
- Comparing squared values efficiently
- Reusing the Binary Search pattern
- Solving problems without using built-in square root functions

#### Difficulty Faced

Recognizing that Binary Search can be used on possible answers instead of only on sorted arrays.

#### Complexity

Time Complexity: O(log n)

Space Complexity: O(1)

---

## Overall Learning

Today's problems reinforced my understanding of Binary Search by showing that it isn't limited to searching in arrays. I learned how the same algorithm can efficiently solve mathematical problems by narrowing down the range of possible answers.

## Status

✅ Both problems accepted on LeetCode

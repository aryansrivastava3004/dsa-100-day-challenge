# Day 40 - Implement Stack using Queues & Implement Queue using Stacks

## Problems

### 1. LeetCode 225 - Implement Stack using Queues

**Topic:** Stack, Queue, Design

#### Approach

Use a single queue to simulate stack behavior. After inserting a new element, rotate the queue so that the newly added element moves to the front. This ensures that the most recently added element is always removed first.

#### What I Learned

- Simulating a stack using a queue
- Queue rotation technique
- LIFO implementation using FIFO
- Understanding data structure design

#### Difficulty Faced

Understanding how rotating the queue after every insertion allows stack operations to work correctly while using only queue operations.

#### Complexity

Push: O(n)

Pop: O(1)

Top: O(1)

Empty: O(1)

Space Complexity: O(n)

---

### 2. LeetCode 232 - Implement Queue using Stacks

**Topic:** Queue, Stack, Design

#### Approach

Maintain two stacks:
- **Input Stack** for inserting elements.
- **Output Stack** for removing elements.

Transfer elements from the input stack to the output stack only when the output stack becomes empty. This preserves FIFO order while keeping operations efficient.

#### What I Learned

- Implementing a queue using two stacks
- Lazy transfer strategy
- FIFO implementation using LIFO
- Amortized analysis of operations

#### Difficulty Faced

Understanding why transferring elements only when necessary improves efficiency instead of moving them after every operation.

#### Complexity

Push: O(1)

Pop: O(1) (Amortized)

Peek: O(1) (Amortized)

Empty: O(1)

Space Complexity: O(n)

---

## Overall Learning

Today's problems helped me understand that data structures can often be built using other data structures. By implementing a stack with queues and a queue with stacks, I gained a deeper understanding of how LIFO and FIFO behaviors work internally and how efficient design choices can optimize performance.

## Status

✅ Both problems accepted on LeetCode

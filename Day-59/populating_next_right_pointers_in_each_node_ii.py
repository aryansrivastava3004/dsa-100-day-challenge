from collections import deque

class Solution:
    def connect(self, root):

        if not root:
            return root

        queue = deque([root])

        while queue:

            prev = None

            for _ in range(len(queue)):

                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            prev.next = None

        return root

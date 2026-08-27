from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):

        if not root:
            return 0

        queue = deque([(root, 0)])
        max_width = 0

        while queue:

            level_start = queue[0][1]
            level_end = queue[-1][1]

            max_width = max(
                max_width,
                level_end - level_start + 1
            )

            for _ in range(len(queue)):

                node, index = queue.popleft()

                if node.left:
                    queue.append(
                        (node.left, 2 * index)
                    )

                if node.right:
                    queue.append(
                        (node.right, 2 * index + 1)
                    )

        return max_width

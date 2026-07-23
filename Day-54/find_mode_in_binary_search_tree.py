class Solution:
    def findMode(self, root):

        frequency = {}

        def dfs(node):

            if not node:
                return

            frequency[node.val] = frequency.get(node.val, 0) + 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_frequency = max(frequency.values())

        return [
            value
            for value, count in frequency.items()
            if count == max_frequency
        ]

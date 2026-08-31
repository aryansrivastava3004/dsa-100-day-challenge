class Solution:
    def findDuplicateSubtrees(self, root):

        count = {}
        result = []

        def dfs(node):

            if not node:
                return "#"

            left = dfs(node.left)
            right = dfs(node.right)

            key = f"{node.val},{left},{right}"

            count[key] = count.get(key, 0) + 1

            if count[key] == 2:
                result.append(node)

            return key

        dfs(root)

        return result

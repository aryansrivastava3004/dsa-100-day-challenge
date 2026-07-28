class Solution:
    def pathSum(self, root, targetSum):

        result = []

        def dfs(node, currentPath, currentSum):

            if not node:
                return

            currentPath.append(node.val)
            currentSum += node.val

            if not node.left and not node.right and currentSum == targetSum:
                result.append(currentPath[:])

            dfs(node.left, currentPath, currentSum)
            dfs(node.right, currentPath, currentSum)

            currentPath.pop()

        dfs(root, [], 0)

        return result

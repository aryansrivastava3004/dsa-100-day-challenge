class Solution:
    def longestUnivaluePath(self, root):

        longest = 0

        def dfs(node):
            nonlocal longest

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left_path = 0
            right_path = 0

            if node.left and node.left.val == node.val:
                left_path = left + 1

            if node.right and node.right.val == node.val:
                right_path = right + 1

            longest = max(longest, left_path + right_path)

            return max(left_path, right_path)

        dfs(root)

        return longest

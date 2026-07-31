class Solution:
    def countNodes(self, root):

        if not root:
            return 0

        left = root.left
        right = root.right

        leftHeight = 0
        rightHeight = 0

        while left:
            leftHeight += 1
            left = left.left

        while right:
            rightHeight += 1
            right = right.right

        if leftHeight == rightHeight:
            return (1 << (leftHeight + 1)) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

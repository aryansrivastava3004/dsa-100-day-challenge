class Solution:
    def getMinimumDifference(self, root):

        self.prev = None
        self.minimum = float("inf")

        def inorder(node):

            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.minimum = min(self.minimum, node.val - self.prev)

            self.prev = node.val

            inorder(node.right)

        inorder(root)

        return self.minimum

class Solution:
    def bstFromPreorder(self, preorder):

        index = 0

        def build(bound):
            nonlocal index

            if index == len(preorder) or preorder[index] > bound:
                return None

            root = TreeNode(preorder[index])
            index += 1

            root.left = build(root.val)
            root.right = build(bound)

            return root

        return build(float("inf"))

class Solution:
    def increasingBST(self, root):

        dummy = TreeNode(0)
        current = dummy

        def inorder(node):
            nonlocal current

            if not node:
                return

            inorder(node.left)

            current.right = TreeNode(node.val)
            current = current.right

            inorder(node.right)

        inorder(root)

        return dummy.right

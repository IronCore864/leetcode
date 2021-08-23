class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0

        def traverse(node):
            nonlocal s
            if not node:
                return
            traverse(node.right)
            node.val += s
            s = node.val
            traverse(node.right)

        traverse(root)
        return root

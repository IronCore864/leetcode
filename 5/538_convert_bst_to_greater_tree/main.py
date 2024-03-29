from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        res = 0

        def traverse(n):
            nonlocal res
            if not n:
                return None

            traverse(n.right)
            res += n.val
            n.val = res
            traverse(n.left)

        traverse(root)
        return root

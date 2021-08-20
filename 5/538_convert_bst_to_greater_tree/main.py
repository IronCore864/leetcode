from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root):
        if not root:
            return None

        self.traverse(root.right)
        self.ans += root.val
        root.val = self.ans
        self.traverse(root.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ans = 0
        self.traverse(root)
        return root

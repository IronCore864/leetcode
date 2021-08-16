from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left, root.right = None, left

        while root.right:
            root = root.right

        root.right = right


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n21, n22 = TreeNode(2), TreeNode(5)
    n1.left, n1.right = n21, n22
    n21.left, n21.right = TreeNode(3), TreeNode(4)
    n22.right = TreeNode(6)

    s.flatten(n1)
    while n1:
        print(n1.val)
        n1 = n1.right

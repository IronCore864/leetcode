from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == '__main__':
    s = Solution()

    n1, n2, n3, n4, n5, n6, n7 = TreeNode(4), TreeNode(2), TreeNode(
        7), TreeNode(1), TreeNode(3), TreeNode(6), TreeNode(9)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7

    res = s.invertTree(n1)
    print(res.val)
    print(res.left.val)
    print(res.right.val)
    print(res.left.left.val)
    print(res.left.right.val)
    print(res.right.left.val)
    print(res.right.right.val)

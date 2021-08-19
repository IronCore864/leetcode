from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        self.i += 1
        if self.i == self.k:
            self.res = root.val
            return

        self.inorder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.k = k
        self.inorder(root)
        return self.res


if __name__ == '__main__':
    s = Solution()
    root, n1, n2, n3 = TreeNode(3), TreeNode(1), TreeNode(4), TreeNode(2)
    root.left, root.right = n1, n2
    n1.right = n3
    print(s.kthSmallest(root, 1))

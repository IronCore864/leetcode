import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = -sys.maxint

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathContaining(root)
        return self.res

    def maxPathContaining(self, n):
        if n is None:
            return 0
        left = max(self.maxPathContaining(n.left), 0)
        right = max(self.maxPathContaining(n.right), 0)
        self.res = max(self.res, left + n.val + right)
        return max(left, right) + n.val


s = Solution()
n1 = TreeNode(1)
n21 = TreeNode(-2)
n22 = TreeNode(-3)
n31 = TreeNode(1)
n32 = TreeNode(3)
n33 = TreeNode(-2)
n41 = TreeNode(-1)
n1.left = n21
n1.right = n22
n21.left = n31
n21.right = n32
n22.left = n33
n22.right = None
n31.left = n41

print s.maxPathSum(n1)

import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def valid(self, root, min_val, max_val):
        if root is None:
            return True
        if root.val >= max_val or root.val <= min_val:
            return False
        return self.valid(root.left, min_val, root.val) and self.valid(root.right, root.val, max_val)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, -sys.maxint - 1, sys.maxint)

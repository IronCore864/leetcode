import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = TreeNode(-sys.maxint - 1)

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        if self.first is None and self.prev.val > root.val:
            self.first = self.prev
        if self.first is not None and self.prev.val > root.val:
            self.second = root
        self.prev = root
        self.traverse(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

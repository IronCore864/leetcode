class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.num = 0
        self.count = 0

    def in_order(self, root):
        if root.left:
            self.in_order(root.left)
        self.count -= 1
        if self.count == 0:
            self.num = root.val
            return
        if root.right:
            self.in_order(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = k
        self.in_order(root)
        return self.num

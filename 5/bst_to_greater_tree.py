# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    sum = 0

    def convert(self, cur):
        if not cur:
            return
        self.convert(cur.right)
        cur.val += self.sum
        self.sum = cur.val
        self.convert(cur.left)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert(root)
        return root

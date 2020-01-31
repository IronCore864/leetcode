import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    previous_val = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.minDiffInBST(root.left)
        self.result = min(self.result, root.val-self.previous_val)
        self.previous_val = root.val
        if root.right:
            self.minDiffInBST(root.right)


        return self.result
        

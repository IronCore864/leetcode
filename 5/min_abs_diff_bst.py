# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution:
    min_diff = sys.maxsize
    prev = -1

    def getMinimumDifference(self, root):
        if root is None:
            return self.min_diff

        self.getMinimumDifference(root.left)

        if self.prev != -1:
            self.min_diff = min(self.min_diff, root.val - self.prev)

        self.prev = root.val

        self.getMinimumDifference(root.right)

        return self.min_diff

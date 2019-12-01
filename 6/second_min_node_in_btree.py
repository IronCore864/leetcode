# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def second_min(root, val):
            if not root.left:
                if root.val != val:
                    return root.val
                else:
                    return sys.maxsize
            else:
                return min(second_min(root.left, val), second_min(root.right, val))
        
        res = second_min(root, root.val)
        
        return res if res != sys.maxsize else -1
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0
        def helper(root):
            if not root:
                return 0
            
            left_side = helper(root.left)
            right_side = helper(root.right)
            
            left = (left_side + 1) if root.left and root.val == root.left.val else 0
            right = (right_side + 1) if root.right and root.val == root.right.val else 0
            
            self.result = max(self.result, left + right)
            
            return max(left, right)
        
        helper(root)
        return self.result

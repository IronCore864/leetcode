# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:  
        s = {}
        
        def search(node, s):
            if not node:
                return False
            diff = k - node.val
            if diff in s:
                return True
            s[node.val] = True
            return search(node.left, s) or search(node.right, s)
        
        return search(root, s)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTreesRecursive(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        
        stack = [(t1, t2)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 or not n2:
                continue
            n1.val += n2.val
            
            if not n1.left:
                n1.left = n2.left
            else:
                stack.append((n1.left, n2.left))
            if not n1.right:
                n1.right = n2.right
            else:
                stack.append((n1.right, n2.right))
        return t1

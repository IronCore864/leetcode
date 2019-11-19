# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        
        row = [root]
        res = []
        while row:
            sum = 0
            nextrow = []
            for n in row:
                sum += n.val
                if n.left:
                    nextrow.append(n.left)
                if n.right:
                    nextrow.append(n.right)
            res.append(sum/len(row))
            row = nextrow
        return res

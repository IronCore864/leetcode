"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if root.children == None or root.children == []:
            return 1
        res = 0
        children = [root]
        while children != []:
            new_children = []
            for n in children:
                new_children += n.children
            children = new_children
            res+=1
        return res

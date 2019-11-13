"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while len(stack)>0:
            current = stack.pop()
            res.append(current.val)
            for node in current.children[::-1]:
                stack.append(node)
        return res

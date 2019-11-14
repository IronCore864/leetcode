"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            current = stack.pop()
            res.append(current.val)
            if current.children:
                stack += current.children
        return res[::-1]

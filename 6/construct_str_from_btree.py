# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        def print_node(t: TreeNode):
            if not t.left and not t.right:
                return "{}".format(t.val)
            elif t.left and not t.right:
                return "{}({})".format(t.val, print_node(t.left))
            elif t.right and not t.left:
                return "{}()({})".format(t.val, print_node(t.right))
            else:
                return "{}({})({})".format(t.val, print_node(t.left), print_node(t.right))
        return print_node(t)

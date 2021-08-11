import sys
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # The in-order traverse of a BST is sorted.
        # Find the two abnormal positions and remember them,
        # then swap.
        first, second, previous = None, None, TreeNode(-sys.maxsize)

        def in_order_traverse(node):
            nonlocal first, second, previous

            if not node:
                return

            in_order_traverse(node.left)

            if first is None and previous.val > node.val:
                first = previous
            if first is not None and previous.val > node.val:
                second = node
            previous = node

            in_order_traverse(node.right)

        in_order_traverse(root)
        first.val, second.val = second.val, first.val

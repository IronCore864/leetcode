from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_min_node(self, root):
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            min_node = self.get_min_node(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root

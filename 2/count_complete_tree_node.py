class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def height(self, root):
        return -1 if not root else 1 + self.height(root.left)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = 0
        h = self.height(root)

        while root:
            # last node is in the right subtree
            # add root and 2**h-1 of the left subtree, and add the right subtree recursively
            if self.height(root.right) == h - 1:
                nodes += 1 << h
                root = root.right
            # last node is in the left subtree
            # add root and 2**(h-1)-1 of the right subtree, and add the left subtree recursively
            else:
                nodes += 1 << h - 1
                root = root.left
            h -= 1

        return nodes

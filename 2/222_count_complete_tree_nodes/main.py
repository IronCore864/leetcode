from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def nodes(self, height):
        return 2 ** height - 1

    def height(self, root):
        return 0 if not root else 1 + self.height(root.left)

    def countNodes(self, root):
        res = 0
        h = self.height(root)

        while root:
            # last node is in the right subtree
            # add root and left subtree, and add the right subtree recursively
            if self.height(root.right) == h - 1:
                res += 1
                res += self.nodes(h-1)
                root = root.right
            # last node is in the left subtree
            # add root and right subtree, and add the left subtree recursively
            else:
                res += 1
                res += self.nodes(h-2)
                root = root.left
            h -= 1

        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    root.left.left, root.left.right = TreeNode(4), TreeNode(5)
    root.right.left = TreeNode(6)

    s = Solution()

    print(s.countNodes(root))

import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True

        stack = []

        pre = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right

        return True

    def recursive(self, root):
        def valid(root, lo, hi):
            if not root:
                return True
            if not (lo < root.val < hi):
                return False
            return valid(root.left, lo, root.val) and valid(root.right, root.val, hi)
        return valid(root, -sys.maxsize, sys.maxsize)


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert s.isValidBST(root) == True

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert s.isValidBST(root) == False

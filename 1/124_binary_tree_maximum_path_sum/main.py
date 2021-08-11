import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        res = -sys.maxsize

        def max_path_containing(node):
            nonlocal res

            if node is None:
                return 0

            left = max(max_path_containing(node.left), 0)
            right = max(max_path_containing(node.right), 0)

            res = max(res, left + node.val + right)
            # only one branch with node
            return max(left, right) + node.val

        max_path_containing(root)
        return res


s = Solution()
n1 = TreeNode(1)
n21 = TreeNode(-2)
n22 = TreeNode(-3)
n31 = TreeNode(1)
n32 = TreeNode(3)
n33 = TreeNode(-2)
n41 = TreeNode(-1)
n1.left = n21
n1.right = n22
n21.left = n31
n21.right = n32
n22.left = n33
n22.right = None
n31.left = n41

print(s.maxPathSum(n1))

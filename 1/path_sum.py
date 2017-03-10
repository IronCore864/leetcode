class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


n1 = TreeNode(5)
n21 = TreeNode(4)
n22 = TreeNode(8)
n31 = TreeNode(11)
n32 = TreeNode(13)
n33 = TreeNode(4)
n41 = TreeNode(7)
n42 = TreeNode(2)
n43 = TreeNode(1)

n1.left = n21
n1.right = n22
n21.left = n31
n22.left = n32
n22.right = n33
n31.left = n41
n31.right = n42
n33.right = n43

s = Solution()
print s.hasPathSum(n1, 22)

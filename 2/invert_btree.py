class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(7)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(9)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7

s = Solution()
res = s.invertTree(n1)
print(res.val)
print(res.left.val)
print(res.right.val)
print(res.left.left.val)
print(res.left.right.val)
print(res.right.left.val)
print(res.right.right.val)

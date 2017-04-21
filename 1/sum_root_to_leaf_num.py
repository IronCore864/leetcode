class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = 0
        self.stack = []

    def preorder(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.stack.append(root)

        if root.left is None and root.right is None:
            self.res += int(''.join(str(i.val) for i in self.stack))

        if root.left:
            self.preorder(root.left)

        if root.right:
            self.preorder(root.right)

        self.stack.pop()

    def sumNumbers(self, root):
        self.preorder(root)
        return self.res


s = Solution()

# n1 = TreeNode(4)
# n2 = TreeNode(9)
# n3 = TreeNode(0)
# n4 = TreeNode(1)
#
# n1.left = n2
# n1.right = n3
# n2.right = n4
#
# print s.sumNumbers(n1)

n1 = TreeNode(2)
n2 = TreeNode(0)
n3 = TreeNode(0)

n1.left = n2
n1.right = n3
print s.sumNumbers(n1)

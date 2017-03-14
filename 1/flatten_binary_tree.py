class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        if root.left is None:
            self.flatten(root.right)
        else:
            self.flatten(root.left)
            prev_right = root.right
            root.right = root.left
            root.left = None
            last = root
            while last.right is not None:
                last = last.right
            last.right = prev_right
            self.flatten(prev_right)

        return root


n1 = TreeNode(1)
n21 = TreeNode(2)
n22 = TreeNode(5)
n31 = TreeNode(3)
n32 = TreeNode(4)
n33 = TreeNode(6)

n1.left = n21
n1.right = n22
n21.left = n31
n21.right = n32
n22.right = n33

s = Solution()
root = s.flatten(n1)
while root:
    print root.val
    root = root.right

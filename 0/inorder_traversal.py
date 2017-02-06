class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        lnodes = []

        while len(lnodes) != 0 or root is not None:
            if root is not None:
                lnodes.append(root)
                root = root.left
            else:
                root = lnodes.pop()
                res.append(root.val)
                root = root.right

        return res


s = Solution()
root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
root.right = n1
n1.left = n2

print s.inorderTraversal(root)

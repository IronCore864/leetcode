class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal_none_recursive(self, root):
        s = []
        res = []
        last_visited = None

        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:
                peek = s[-1]
                if peek.right is not None and last_visited != peek.right:
                    root = peek.right
                else:
                    res.append(peek.val)
                    last_visited = s.pop()

        return res

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


s = Solution()
root = TreeNode(1)
n1r = TreeNode(2)
n2l = TreeNode(3)
root.right = n1r
n1r.left = n2l
print s.postorderTraversal(root)
print s.postorderTraversal_none_recursive(root)

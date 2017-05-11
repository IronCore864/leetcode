class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal_none_recursive(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


s = Solution()
root = TreeNode(1)
n1r = TreeNode(2)
n2l = TreeNode(3)
root.right = n1r
n1r.left = n2l
print s.preorderTraversal(root)

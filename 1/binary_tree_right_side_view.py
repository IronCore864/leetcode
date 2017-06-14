class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        current = [root]
        next = []
        res = []
        while current:
            for node in current:
                if node:
                    if node.left:
                        next.append(node.left)
                    if node.right:
                        next.append(node.right)
            res.append(current[-1].val)
            current = next
            next = []
        return res


root = TreeNode(1)
l11 = TreeNode(2)
l12 = TreeNode(3)
l21 = TreeNode(5)
l22 = TreeNode(4)
root.left = l11
root.right = l12
l11.right = l21
l12.right = l22

s = Solution()
print(s.rightSideView(root))

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 209 / 209 test cases passed.
# Status: Accepted
# Runtime: 42 ms
class Solution(object):
    def __init__(self):
        self.res = []

    def helper(self, root, path):
        path = path + '->' + str(root.val) if path else str(root.val)
        if not root.left and not root.right:
            self.res.append(path)
            return
        if root.left:
            self.helper(root.left, path)
        if root.right:
            self.helper(root.right, path)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return self.res
        self.helper(root, "")
        return self.res


# test
# 1
# /   \
# 2     3
#  \
#   5
root = TreeNode(1)
n11 = TreeNode(2)
n12 = TreeNode(3)
n21 = TreeNode(5)
root.left = n11
root.right = n12
n11.right = n21

s = Solution()
# ["1->2->5", "1->3"]
print(s.binaryTreePaths(root))

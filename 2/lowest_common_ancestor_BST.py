class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p

        if p.val < root.val < q.val or p.val == root.val or q.val == root.val:
            return root

        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)


#      _______6______
#     /              \
#  ___2__          ___8__
# /      \        /      \
# 0      _4       7       9
#       /  \
#       3   5

root = TreeNode(6)
n11 = TreeNode(2)
n12 = TreeNode(8)
n21 = TreeNode(0)
n22 = TreeNode(4)
n23 = TreeNode(7)
n24 = TreeNode(9)
n31 = TreeNode(3)
n32 = TreeNode(5)
root.left = n11
root.right = n12
n11.left = n21
n11.right = n22
n12.left = n23
n12.right = n24
n22.left = n31
n22.right = n32

s = Solution()
print(s.lowestCommonAncestor(root, n31, n24).val)
print(s.lowestCommonAncestor(root, n11, n22).val)

# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 115 ms

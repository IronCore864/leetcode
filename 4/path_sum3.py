class Solution(object):
    def pathSumFrom(self, node, s):
        if not node:
            return 0

        return int(node.val == s) + \
               self.pathSumFrom(node.left, s - node.val) + \
               self.pathSumFrom(node.right, s - node.val)

    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSumFrom(root, s) + self.pathSum(root.left, s) + self.pathSum(root.right, s)

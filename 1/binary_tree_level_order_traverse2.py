class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # corner case: none input
        if root is None:
            return []

        current_level = [root]

        res = []

        while current_level != []:
            # traverse current level
            line_res = []
            for node in current_level:
                line_res.append(node.val)
            res.append(line_res)

            # get all nodes belong to next level
            next_level = []
            for node in current_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            # incremental
            current_level = next_level
        res.reverse()
        return res


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

s = Solution()
res = s.levelOrderBottom(n1)
print res

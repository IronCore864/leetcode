class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # corner case: none input
        if root is None:
            return []

        current_level = [root]

        res = []

        order = 0
        while current_level != []:
            # traverse current level
            line_res = []
            for node in current_level:
                line_res.append(node.val)
            if order % 2 == 1:
                line_res.reverse()
            res.append(line_res)

            # get all nodes belong to next level
            next_level = []
            order += 1
            for node in current_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            # incremental
            current_level = next_level

        return res


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n1.right = n3
n2.left = n4
n3.right = n5

s = Solution()
res = s.zigzagLevelOrder(n1)
print res

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder is None or len(preorder) == 0:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])

        root_in_inorder_index = inorder.index(preorder[0])

        left_in = inorder[:root_in_inorder_index]
        left_pre = preorder[1:1 + len(left_in)]

        right_pre = preorder[1 + len(left_in):]
        right_in = inorder[root_in_inorder_index + 1:]

        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)

        return root


s = Solution()
res = s.buildTree([1, 2, 5, 3, 6, 7], [2, 5, 1, 6, 3, 7])
print res.val, res.left.val, res.right.val
print res.left.right.val, res.right.left.val, res.right.right.val

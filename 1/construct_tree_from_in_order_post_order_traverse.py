class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if postorder is None or len(postorder) == 0:
            return None

        if len(postorder) == 1:
            return TreeNode(postorder[0])

        root = TreeNode(postorder[-1])

        root_in_inorder_index = inorder.index(postorder[-1])

        left_in = inorder[:root_in_inorder_index]
        left_post = postorder[0:len(left_in)]

        right_post = postorder[len(left_in):-1]
        right_in = inorder[root_in_inorder_index + 1:]

        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)

        return root


s = Solution()
res = s.buildTree([4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1])
print res.val
print res.left.val, res.right.val
print res.left.left.val, res.left.right.val, res.right.left.val, res.right.right.val

from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return []

        # preorder path to count dict
        self.c = defaultdict(int)
        self.res = []
        self.preorder(root)
        return self.res

    def preorder(self, root):
        if not root:
            return '#'

        pre_order_path = "{}-{}-{}".format(
            str(root.val),
            self.preorder(root.left),
            self.preorder(root.right)
        )

        if self.c.get(pre_order_path) == 1:
            self.res.append(root)

        self.c[pre_order_path] += 1
        return pre_order_path


# for testing
def print_tree(root):
    if not root:
        return '#'
    else:
        return "{}-{}-{}".format(
            root.val, print_tree(root.left), print_tree(root.right))


if __name__ == '__main__':
    s = Solution()

    root, n1, n2 = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left, root.right = n1, n2
    n3, n4, n5, n6 = TreeNode(4), TreeNode(2), TreeNode(4), TreeNode(4)
    n1.left = n3
    n2.left, n2.right = n4, n5
    n4.left = n6

    res = s.findDuplicateSubtrees(root)

    for root in res:
        print(print_tree(root))

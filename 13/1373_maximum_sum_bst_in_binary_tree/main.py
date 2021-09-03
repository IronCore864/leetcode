from typing import Optional
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/discuss/531800/Python-Easy-traversal-with-explanation
        https://labuladong.gitbook.io/algo/mu-lu-ye-1/mu-lu-ye-1/hou-xu-bian-li
        """
        res = 0

        def traverse(root):
            """
            return: is_bst(0: no, 1: yes and None, 2: yes), left_min, right_max, sum
            """
            nonlocal res
            if not root:
                return 1, None, None, 0

            lb, ll, lh, ls = traverse(root.left)
            rb, rl, rh, rs = traverse(root.right)

            if ((lb == 2 and lh < root.val) or lb == 1) and ((rb == 2 and rl > root.val) or rb == 1):
                s = root.val + ls + rs
                res = max(res, s)
                return 2, (ll if ll is not None else root.val), (rh if rh is not None else root.val), s
            return 0, None, None, None

        traverse(root)
        return res


def test():
    root, n1, n2 = TreeNode(1), TreeNode(4), TreeNode(3)
    root.left, root.right = n1, n2
    n3, n4, n5, n6 = TreeNode(2), TreeNode(4), TreeNode(2), TreeNode(5)
    n7, n8 = TreeNode(4), TreeNode(6)
    n1.left, n1.right, n2.left, n2.right = n3, n4, n5, n6
    n6.left, n6.right = n7, n8

    s = Solution()
    print(s.maxSumBST(root))


if __name__ == '__main__':
    test()

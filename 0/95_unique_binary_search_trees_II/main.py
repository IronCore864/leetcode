from sys import builtin_module_names
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(self, nums) -> List[Optional[TreeNode]]:
        n = len(nums)

        if n == 0:
            return [None]

        if n == 1:
            return [TreeNode(nums[0])]

        res = []
        for i in range(n):
            lnums = nums[0:i]
            rnums = nums[i+1:]
            for l in self.build_tree(lnums):
                for r in self.build_tree(rnums):
                    root = TreeNode(nums[i])
                    root.left, root.right = l, r
                    res.append(root)
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums = [i for i in range(1, n+1)]
        return self.build_tree(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.generateTrees(3))

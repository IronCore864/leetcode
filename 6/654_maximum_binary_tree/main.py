from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        root_val = max(nums)
        root_val_index = nums.index(root_val)
        root = TreeNode(root_val)
        root.left = self.constructMaximumBinaryTree(nums[0:root_val_index])
        root.right = self.constructMaximumBinaryTree(nums[root_val_index+1:])
        return root


if __name__ == '__main__':
    s = Solution()
    root = s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])

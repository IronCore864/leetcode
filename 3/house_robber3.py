from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob_sub(self, root) -> List[int]:
        if not root:
            return [0, 0]

        left = self.rob_sub(root.left)
        right = self.rob_sub(root.right)
        res = [0, 0]

        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]

        return res

    def rob(self, root: TreeNode) -> int:
        res = self.rob_sub(root)
        return max(res)


if __name__ == "__main__":
    root = TreeNode(4)
    l11 = TreeNode(1)
    l21 = TreeNode(2)
    l31 = TreeNode(3)

    root.left = l11
    l11.left = l21
    l21.left = l31

    s = Solution()
    print(s.rob(root))

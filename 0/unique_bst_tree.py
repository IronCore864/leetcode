class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generate_tree_helper(self, nums):
        if len(nums) == 0:
            return [None]
        if len(nums) == 1:
            return [TreeNode(nums[0])]
        res = []
        for num in nums:
            left_nums = []
            right_nums = []
            for i in nums:
                if i < num:
                    left_nums.append(i)
                if i > num:
                    right_nums.append(i)
            left_res = self.generate_tree_helper(left_nums)
            right_res = self.generate_tree_helper(right_nums)
            for i in left_res:
                for j in right_res:
                    root = TreeNode(num)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generate_tree_helper(range(1, n + 1))


s = Solution()
res = s.generateTrees(3)


def print_tree(root):
    if root:
        print root.val
        if root.left is None and root.right is not None:
            print None
            print_tree(root.right)
        if root.left is None and root.right is None:
            return
        if root.left is not None:
            print_tree(root.left)
            print_tree(root.right)


for r in res:
    print_tree(r)
    print

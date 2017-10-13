class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 0 if not nums else sum(nums) - min(nums) * len(nums)


s = Solution()
print(s.minMoves([1, 2, 3]))

# https://discuss.leetcode.com/topic/66737/it-is-a-math-question
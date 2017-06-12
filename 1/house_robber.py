class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        previous = nums[0]
        now = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res = max(previous + nums[i], now)
            previous = now
            now = res

        return res


s = Solution()
print(s.rob([2, 1, 1, 2]))

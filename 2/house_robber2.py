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

        def rob(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now

        return max(rob(nums[1:]), rob(nums[:-1]))

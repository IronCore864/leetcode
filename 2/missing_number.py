class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        sum = (0 + l) * (l + 1) / 2
        for n in nums:
            sum -= n

        return sum

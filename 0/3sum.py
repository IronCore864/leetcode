class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        i = 0
        j = 1
        res = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[i] + nums[j] > 0:
                    break
                expected = 0 - nums[i] - nums[j]
                if expected in nums[j + 1:] and not [nums[i], nums[j], expected] in res:
                    res.append([nums[i], nums[j], expected])
        return res


s = Solution()
print s.threeSum(
    [-6, -8, -9, 4, -14, 6, -10, 7, 12, 13, 4, 9, 7, 14, -12, 7, 0, 14, -1, -3, 2, 2, -3, 11, -6, -10, -13, -13, 1, -9,
     2, 2, -2, 8, -9, 0, -9, -12, 14, 10])


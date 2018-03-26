class Solution:
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss, res, i = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                res += 1
        return res


s = Solution()
print(s.minPatches([1,2,31,33], 2147483647))
# print(s.minPatches([1, 5, 10], 20))
# print(s.minPatches([1, 2, 2], 5))
# print(s.minPatches([], 7))

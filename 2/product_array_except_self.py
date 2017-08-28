class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        tmp = 1
        for i in range(0, len(nums)):
            res[i] *= tmp
            tmp *= nums[i]

        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]

        return res


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))

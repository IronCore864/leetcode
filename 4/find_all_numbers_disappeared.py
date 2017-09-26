class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            nums[idx] = -nums[idx] if nums[idx] > 0 else nums[idx]
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        return res

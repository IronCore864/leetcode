class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                res = max(res, counter)
                counter = 0
        res = max(res, counter)
        return res

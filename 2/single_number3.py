class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff = 0
        for num in nums:
            diff ^= num
        # get a set bit
        diff &= -diff

        res = [0, 0]
        for num in nums:
            if (num & diff) == 0:
                # bit is not set
                res[0] ^= num
            else:
                res[1] ^= num
        return res

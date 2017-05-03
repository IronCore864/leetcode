class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            sum = 0
            for j in xrange(len(nums)):
                if (nums[j] >> i) & 1 == 1:
                    sum += 1
                    sum %= 3
            if sum != 0:
                res |= sum << i
        return -(2 ** 32 - res) if (res >> 31) & 1 == 1 else res


s = Solution()
print s.singleNumber([1, 1, 1, 3, 3, 3, 4, 4, 4, 8])
print s.singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])

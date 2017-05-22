class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = nums[0]
        imax = r
        imin = r
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])
            r = max(r, imax)
        return r


s = Solution()
print s.maxProduct([0, -2, 0])

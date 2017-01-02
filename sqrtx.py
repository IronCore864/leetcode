class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        h = 0
        while 1 << h * 1 << h <= x:
            h += 1
        h -= 1
        bit = h - 1
        res = 1 << h

        while bit >= 0:
            if (res | (1 << bit)) * (res | (1 << bit)) <= x:
                res |= 1 << bit
            bit -= 1
        return res


s = Solution()
print s.mySqrt(81)
print s.mySqrt(122)

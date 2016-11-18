class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        maxint = 2147483647
        if divisor == 0:
            return maxint
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend if -dividend < maxint else maxint

        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            negative = False
        else:
            negative = True

        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp = divisor
            count = 1
            while tmp <= dividend:
                count <<= 1
                tmp <<= 1
            res += count >> 1
            dividend -= tmp >> 1
        return res if not negative else -res


s = Solution()
print s.divide(2, 2)
print s.divide(2147483647, 2)

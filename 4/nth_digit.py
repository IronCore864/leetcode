class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        count = 9
        start = 1
        while n > l * count:
            n -= l * count
            l += 1
            count *= 10
            start *= 10
        start += (n - 1) // l
        s = str(start)
        return int(s[(n - 1) % l])


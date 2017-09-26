# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def _helper(self, l, r):
        m = (l + r) / 2
        res = guess(m)
        if res == 0:
            return m
        elif res > 0:
            return self._helper(m + 1, r)
        else:
            return self._helper(l, m - 1)

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self._helper(1, n)

from sys import maxsize as MAXINT


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        cntPerfectSquares = [0]

        while len(cntPerfectSquares) <= n:
            m = len(cntPerfectSquares)
            cntSquares = MAXINT
            i = 1
            while i * i <= m:
                cntSquares = min(cntSquares, cntPerfectSquares[m - i * i] + 1)
                i += 1
            cntPerfectSquares.append(cntSquares)
        return cntPerfectSquares[n]


s = Solution()
print(s.numSquares(12))
print(s.numSquares(13))

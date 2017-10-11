import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.floor(-0.5 + math.sqrt(2 * n + 0.25)))


s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))

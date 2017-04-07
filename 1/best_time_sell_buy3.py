import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell1 = 0
        sell2 = 0
        buy1 = - sys.maxint
        buy2 = - sys.maxint

        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2


s = Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])

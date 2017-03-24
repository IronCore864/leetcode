import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = sys.maxint
        for i in xrange(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            max_profit = max(max_profit, prices[i]-min_price)

        if max_profit < 0:
            return 0
        else:
            return max_profit


s = Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


s = Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])
print s.maxProfit([1, 7, 2, 3, 6, 7, 6, 7])

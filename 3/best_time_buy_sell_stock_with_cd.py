class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)

        if n < 2:
            return 0

        noStock = 0
        noStockCD = float('-inf')
        haveStock = float('-inf')

        for p in prices:
            # haveStock - do nothing - haveStock
            # noStock - buy - haveStock
            haveStock = max(haveStock, noStock - p)
            # noStock - do nothing - noStock
            # noStockCD - do nothing - noStock
            noStock = max(noStock, noStockCD)
            # haveStock - sell - noStockCD
            noStockCD = p + haveStock

        return max(haveStock, noStock, noStockCD)

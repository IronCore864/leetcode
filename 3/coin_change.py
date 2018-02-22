import sys


class Solution(object):
    def coinChange(self, coins, amount):
        MAX = sys.maxsize
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp_prev = min([dp[i - c] if i - c >= 0 else MAX for c in coins])
            dp[i] = dp_prev+1 if dp_prev != MAX else MAX

        return -1 if dp[amount] == MAX else dp[amount]

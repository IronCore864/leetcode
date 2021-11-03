import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i-c] + 1)

        return dp[-1]if dp[-1] != sys.maxsize else -1


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([2], 3))
    print(s.coinChange([186, 419, 83, 408], 6249))

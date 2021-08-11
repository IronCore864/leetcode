import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [sys.maxsize] * (amount+1)
        res[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    res[i] = min(res[i], res[i-c] + 1)

        if res[amount] == sys.maxsize:
            return -1

        return res[amount]

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n+1):
            a = 1
            b = i - a
            maxProduct = 0
            while a <= b:
                maxProduct = max(maxProduct, max(a, dp[a])*max(b, dp[b]))
                a += 1
                b -= 1
            dp.append(maxProduct)
        return dp[-1]


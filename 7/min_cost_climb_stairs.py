class Solution:
    def minCostClimbingStairs(self, cost):
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[-1]


s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

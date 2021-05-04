class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)

        if l == 0:
            return 0

        # dynamic programming
        # if backtracking/dfs, timeout
        dp = [0] * (l+1)
        # dp[0] = 1 means there is only 1 way to decode an empty string
        # this is only used to calculate d[1] and so on.
        # dp[n] = dp[n-2] (if s[n-2:n] in 10..26) + dp[n-1] (if s[n] in 1..9)
        dp[0] = 1

        for i in range(1, l+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            if i != 1 and '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    assert s.numDecodings('12') == 2
    assert s.numDecodings('226') == 3
    assert s.numDecodings('0') == 0
    assert s.numDecodings('06') == 0

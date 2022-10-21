class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # for each char in the input string, use it as the center of the palindrome
        # expand to left and right and try to get the maximum palindrome
        # note that a palindrome can be "aba" (odd number of length) or "abba" (even)
        for i in range(len(s)):
            tmp = self.max_palindrome_substr(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.max_palindrome_substr(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def longestPalindrome_DP(self, s: str) -> str:
        res = ''
        l = len(s)

        # dp[i][j] means s[i:j+1] is a palindrome
        dp = [[False for _ in range(l)] for _ in range(l)]

        # if i == j it means it's one char and it's a palindrome
        for i in range(l):
            dp[i][i] = True
            res = s[i]

        # reversed range to generate shorter substrings first so that DP can hit more to save cost
        for start in range(l-1, -1, -1):
            for end in range(start+1, l):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if end-start+1 > len(res):
                            res = s[start:end+1]
        return res

    def max_palindrome_substr(self, word, left, right):
        while left >= 0 and right < len(word) and word[left] == word[right]:
            left -= 1
            right += 1
        return word[left + 1:right]


if __name__ == '__main__':
    s = Solution()
    assert s.longestPalindrome('babad') == 'bab'
    print(s.longestPalindrome_DP('babad'))

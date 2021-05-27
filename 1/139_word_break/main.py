class Solution:
    def wordBreak_dfs_slow(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        wordset = set(wordDict)
        res = False

        def dfs(path, index):
            nonlocal res
            if res == True:
                return

            if path == s:
                res = True
                return

            for i in range(index, n+1):
                if s[index:i] in wordset:
                    dfs(path+s[index:i], i)

        dfs("", 0)
        return res

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)

        # dp[i] is True if s[0:i+1] (including s[i]) can be break into dict words
        dp = [False] * n

        for i in range(n):
            for word in wordDict:
                # for each word, see if it matches the string's last part
                word_len = len(word)
                s_last_word = s[i+1-word_len:i+1]
                if s_last_word == word:
                    # it matches from the start of the string
                    if i - word_len == -1:
                        dp[i] = True
                    # or it matches s[i-wordlen+1:i+1], but dp[i-wordlen] can be break into dict words
                    elif i-word_len >= 0 and dp[i-word_len]:
                        dp[i] = True

        return dp[-1]


if __name__ == '__main__':
    s = Solution()

    assert s.wordBreak("leetcode", ["leet", "code"]) == True
    assert s.wordBreak("applepenapple", ["apple", "pen"]) == True
    assert s.wordBreak(
        "catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

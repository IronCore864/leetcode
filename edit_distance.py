class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        d[0][0] = 0

        for i in range(1, n + 1):
            d[0][i] = i

        for i in range(1, m + 1):
            d[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min(d[i - 1][j - 1] + 1, d[i][j - 1] + 1, d[i - 1][j] + 1)
                    # replace, insert, delete
        return d[m][n]


s = Solution()
print s.minDistance("", "")
print s.minDistance("a", "b")
print s.minDistance("", "abc")
print s.minDistance("a", "abc")
print s.minDistance("abc", "def")
print s.minDistance("apple", "banana")

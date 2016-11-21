class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == '':
            return []

        if len(words) == 0:
            return []

        lens = len(s)
        lenword = len(words[0])
        lenwords = len(words) * lenword
        words.sort()

        if lens < lenwords:
            return []

        res = []
        for i in range(0, lens - lenwords + 1):
            if s[i:i + lenword] not in words:
                continue

            substr = s[i:i + lenwords]
            substrs = sorted([substr[j:j + lenword] for j in range(0, lenwords, lenword)])
            if substrs == words:
                res.append(i)
        return res


solution = Solution()
s = 'barfoothefoobarman'
words = ['foo', 'bar']
print solution.findSubstring(s, words)


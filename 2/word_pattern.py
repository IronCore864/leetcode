class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))


s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
# print(s.wordPattern("abba", "dog cat cat fish"))
# print(s.wordPattern("aaaa", "dog cat cat dog"))
# print(s.wordPattern("abba", "dog dog dog dog"))

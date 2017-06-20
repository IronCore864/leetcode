class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return [s.find(i) for i in s] == [t.find(j) for j in t]


s = Solution()
print(s.isIsomorphic('egg', 'add'))
print(s.isIsomorphic('foo', 'bar'))
print(s.isIsomorphic('paper', 'title'))
print(s.isIsomorphic('aa', 'ab'))

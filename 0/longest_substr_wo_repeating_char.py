class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {}
        max_len = 0
        start = 0
        end = 0
        for end in xrange(0, len(s)):
            start = max(index.get(s[end], 0), start)
            max_len = max(max_len, end - start + 1)
            index[s[end]] = end + 1
        return max_len


s = Solution()
print s.lengthOfLongestSubstring('abcabcbb')
print s.lengthOfLongestSubstring('bbbbb')
print s.lengthOfLongestSubstring('pwwkew')
print s.lengthOfLongestSubstring('a')

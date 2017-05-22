class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            ''

        s = s.strip()

        if not s:
            return ''

        return ' '.join(s.strip().split()[::-1])


s = Solution()
print s.reverseWords("the sky is blue")

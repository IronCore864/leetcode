class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None:
            return -1

        if haystack == '' and needle != '':
            return -1

        if needle == '':
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:len(needle) + i] == needle:
                return i
        return -1


s = Solution()
print s.strStr("mississippi", "issi")


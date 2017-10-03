class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        char_counts = {a: s.count(a) for a in s}

        has_odd = False

        res = 0

        for _, count in char_counts.items():
            if count % 2 == 0:
                res += count
            else:
                if not has_odd:
                    res += count
                    has_odd = True
                else:
                    res += (count - 1)

        return res


s = Solution()
print(s.longestPalindrome('abccccdd'))

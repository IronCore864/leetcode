class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k < 2:
            return s

        s = [s[i:i + k][::-1] if i // k % 2 == 0 else s[i:i + k] for i in range(0, len(s), k)]
        return ("".join(s))


s = Solution()
s.reverseStr('abcdefgh', 3)

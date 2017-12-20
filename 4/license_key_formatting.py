class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "")
        first_len = len(S) % K
        if first_len == 0:
            first_len = K
        res = S[0:first_len]
        i = first_len
        while i < len(S):
            res += "-"
            res += S[i:i + K]
            i += K
        return res.upper()


s = Solution()
print(s.licenseKeyFormatting("2-5g-3-J", 2))

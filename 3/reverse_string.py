class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = list(s)
        i, j = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1
        return "".join(r)

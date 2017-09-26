class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum_s, sum_t = 0, 0

        for i in s:
            sum_s += ord(i)

        for i in t:
            sum_t += ord(i)

        return chr(sum_t - sum_s)

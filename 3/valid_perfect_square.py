class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # A square number is 1+3+5+7+...
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0;

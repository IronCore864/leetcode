import sys


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f, s, t = -sys.maxsize, -sys.maxsize, -sys.maxsize
        for i in nums:
            if i > f:
                f, s, t = i, f, s
            elif f > i > s:
                s, t = i, s
            elif s > i > t:
                t = i
            else:
                continue

        return t if t != -sys.maxsize else f

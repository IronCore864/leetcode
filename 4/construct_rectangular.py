from math import ceil, sqrt


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = int(ceil(sqrt(area)))
        while area % L != 0:
            L += 1
        return [L, area // L]

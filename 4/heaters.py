class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for x in sorted(houses):
            while x >= sum(heaters[i:i + 2]) / 2.:
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r


s = Solution()
print(s.findRadius([1, 2, 3, 4], [1, 4]))

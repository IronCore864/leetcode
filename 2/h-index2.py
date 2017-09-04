class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l


s = Solution()
print(s.hIndex([0, 0]))
print(s.hIndex([6]))
print(s.hIndex([6, 5]))
print(s.hIndex([0, 1, 3, 5, 6]))
print(s.hIndex([2, 3, 4, 5, 6]))

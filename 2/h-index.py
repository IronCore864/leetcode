class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        n = len(citations)

        if n == 1:
            return 1 if citations[0] else 0

        citations.sort()
        citations.reverse()

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                continue
            else:
                return i

        return n


s = Solution()
print(s.hIndex([6]))
print(s.hIndex([6, 5]))
print(s.hIndex([6, 5, 3, 1, 0]))
print(s.hIndex([6, 5, 4, 3, 2]))

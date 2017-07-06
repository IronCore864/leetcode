from heapq import heappush, heappop


class Solution(object):
    # https://briangordon.github.io/2014/08/the-skyline-problem.html
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = []
        i, n = 0, len(buildings)
        active = []

        while i < n or active:
            if not active or (i < n and buildings[i][0] <= active[0][1]):
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heappush(active, (-buildings[i][2], buildings[i][1]))
                    i += 1
            else:
                x = active[0][1]
                while active and active[0][1] <= x:
                    heappop(active)
            height = len(active) and -active[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline


s = Solution()
print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))

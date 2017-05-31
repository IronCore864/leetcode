class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        initial_hp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    initial_hp[i][j] = max(1, 1 - dungeon[i][j])
                elif i == m - 1:
                    initial_hp[i][j] = max(1, initial_hp[i][j + 1] - dungeon[i][j])
                elif j == n - 1:
                    initial_hp[i][j] = max(1, initial_hp[i + 1][j] - dungeon[i][j])
                else:
                    initial_hp[i][j] = max(1, min(initial_hp[i + 1][j], initial_hp[i][j + 1]) - dungeon[i][j])
        return initial_hp[0][0]


s = Solution()
dungeon = [[2], [1]]
print s.calculateMinimumHP(dungeon)

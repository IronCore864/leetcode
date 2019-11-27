class Solution:
    def get(self, i, j, M):
        if i < 0 or j < 0 or i >= len(M) or j >= len(M[0]):
            return 0, 0
        return M[i][j], 1

    def avg(self, i, j, M):
        neighbour_sum, neighbour_count = 0, 0
        for row in range(i-1, i+2):
            for col in range(j-1, j+2):
                v, c = self.get(row, col, M)
                neighbour_sum += v
                neighbour_count += c
        return neighbour_sum // neighbour_count

    def imageSmoother(self, M):
        if len(M) == 0 or len(M[0]) == 0:
            return M
        res = [[0 for j in range(len(M[0]))] for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                res[i][j] = self.avg(i, j, M)
        return res

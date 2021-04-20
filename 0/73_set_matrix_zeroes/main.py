class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # if a cell is 0, mark all the cells in the same row and same column as a special character
        # if mark as 0, when processing the next cell,
        # you can't tell if it was 0 originally or was changed by previous operations
        # if, however, during the operation in the same row/column, a cell is already 0, don't change it
        # because his row/column need to be updated too
        # in place, intuitive solution
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = '#'
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = '#'

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0

        # this problem doesn't require return; only for testing/assert purpose
        return matrix


if __name__ == '__main__':
    s = Solution()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

    assert s.setZeroes(matrix) == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

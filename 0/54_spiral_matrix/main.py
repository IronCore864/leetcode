class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        # direction means in which direction to go to find the next available cell which isn't in the output yet
        x, y, direction = 0, 0, 'r'

        # number of rows and columns of the matrix
        m, n = len(matrix), len(matrix[0])

        res.append(matrix[x][y])
        # '#' marks the cell already in the result
        matrix[x][y] = '#'

        # get_next returns the next cell which isn't in the result yet
        # based on the current coordination and the current direction
        def get_next(i, j, direction):
            # if we are moving to the right
            if direction == 'r':
                # if we haven't reached the right border yet
                # (the physical limit which is the size of the matrix, or the cell is already used in the output)
                # keep moving right
                if j < n-1 and matrix[i][j+1] != '#':
                    return i, j+1, direction
                # if we reached the right border, we start moving down if that's possible
                elif i < m-1 and matrix[i+1][j] != '#':
                    return i+1, j, 'd'
                # if we can't move down, it means all cells are already in the output
                else:
                    return -1, -1, None
            # similar logic as above, if we are moving down, continue moving down, or when at border, change direction to up
            if direction == 'd':
                if i < m-1 and matrix[i+1][j] != '#':
                    return i+1, j, direction
                elif j > 0 and matrix[i][j-1] != '#':
                    return i, j-1, 'l'
                else:
                    return -1, -1, None
            if direction == 'l':
                if j > 0 and matrix[i][j-1] != '#':
                    return i, j-1, direction
                elif i > 0 and matrix[i-1][j] != '#':
                    return i-1, j, 'u'
                else:
                    return -1, -1, None
            if direction == 'u':
                if i > 0 and matrix[i-1][j] != '#':
                    return i-1, j, direction
                elif j < n-1 and matrix[i][j+1] != '#':
                    return i, j+1, 'r'
                else:
                    return -1, -1, None

        x, y, direction = get_next(x, y, direction)

        while direction != None:
            res.append(matrix[x][y])
            matrix[x][y] = '#'
            x, y, direction = get_next(x, y, direction)

        return res


if __name__ == '__main__':
    s = Solution()

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert s.spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert s.spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    matrix = [
        [0]
    ]
    assert s.spiralOrder(matrix) == [0]

    matrix = [
        [1, 2],
        [3, 4]
    ]
    assert s.spiralOrder(matrix) == [1, 2, 4, 3]

    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    assert s.spiralOrder(matrix) == [
        1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

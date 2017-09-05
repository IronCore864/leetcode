class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                count = 0
                for ii in range(max(i - 1, 0), min(i + 2, m)):
                    for jj in range(max(j - 1, 0), min(j + 2, n)):
                        count += board[ii][jj] & 1
                if count == 3 or count - board[i][j] == 3:
                    board[i][j] |= 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

        print(board)


s = Solution()
s.gameOfLife(([[1, 1], [1, 0]]))

# since the board has ints but only the 1-bit (0 or 1) is used
# use the 2-bit to store the new state
# at the end, replace the old state with the new state by shifting all values one bit to the right.
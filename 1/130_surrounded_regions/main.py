class Solution:
    def flip(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'

    def solve(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if board[i][j] == 'O':
                board[i][j] = 'T'
                # up
                if i > 0:
                    dfs(i-1, j)
                # down
                if i < m-1:
                    dfs(i+1, j)
                # left
                if j > 0:
                    dfs(i, j-1)
                # right
                if j < n-1:
                    dfs(i, j+1)

        # mark first row and last row boarder 'O's as temporary 'T'
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)
        # mark first column and last column boarder 'O's as temporary 'T'
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)

        # convert temporary 'T' back to 'O' which means these are the 'O's on the boarder or not surrounded
        # and convert surrounded 'O's to 'X's
        self.flip(board)


if __name__ == '__main__':
    s = Solution()
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    s.solve(board)
    print(board)
    assert board == [['X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X'],
                     ['X', 'O', 'X', 'X']]

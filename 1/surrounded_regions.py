class Solution(object):
    def solve(self, board):
        if not board:
            return

        m, n = len(board), len(board[0])
        save = list([ij for k in range(max(m, n)) for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))])

        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                new_line = [c for c in board[i]]
                new_line[j] = 'S'
                board[i] = ''.join(new_line)
                save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
        print board


s = Solution()
board = ["XOXOXO", "OXOXOX", "XOXOXO", "OXOXOX"]
s.solve(board)

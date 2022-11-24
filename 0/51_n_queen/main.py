from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [['.'] * n for _ in range(n)]

        def dfs(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):
                if not safe(row, col):
                    continue
                board[row][col] = 'Q'
                dfs(row + 1)
                board[row][col] = '.'

        def safe(r, c):
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
                if r - i >= 0 and c - i >= 0 and board[r-i][c-i] == 'Q':
                    return False
                if r - i >= 0 and c + i < n and board[r-i][c+i] == 'Q':
                    return False
            return True

        dfs(0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))

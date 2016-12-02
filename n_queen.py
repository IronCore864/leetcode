class Solution(object):
    @staticmethod
    def _safe(row, col, board, n):
        return False if [board[i][col] for i in range(n)].count("Q") > 1 or \
                        [board[i][i - row + col] for i in range(n) if 0 <= i - row + col < n].count("Q") > 1 or \
                        [board[i][row + col - i] for i in range(n) if 0 <= row + col - i < n].count("Q") > 1 else True

    @staticmethod
    def _end(possible):
        for row in possible:
            if len(row) != 0:
                return False
        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        row = 0
        board = [["." for _ in range(n)] for _ in range(n)]
        possible = [range(n) for _ in range(n)]
        res = []

        while not self._end(possible):

            if len(possible[row]) != 0:
                pos = possible[row].pop(0)
                # reset row
                board[row] = ["." for _ in range(n)]
                board[row][pos] = "Q"
                if self._safe(row, pos, board, n):
                    if row == n - 1:
                        res.append(["".join(x) for x in board])
                        continue
                    else:
                        row += 1
                else:
                    continue
            else:
                # reset row
                board[row] = ["." for _ in range(n)]
                # go back to last row
                possible[row] = range(n)
                row -= 1
                if row < 0:
                    break
                continue
        return res


s = Solution()
res = s.solveNQueens(8)
for solution in res:
    print "Solution"
    for row in solution:
        print " ".join(row)
    print ""


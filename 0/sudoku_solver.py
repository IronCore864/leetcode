from copy import deepcopy


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        to_fill = [(x, y) for x in range(0, 9) for y in range(0, 9) if board[x][y] == '.']

        possible = [[None for _ in range(0, 9)] for _ in range(0, 9)]

        i = 0
        while i < len(to_fill):
            x, y = to_fill[i]
            possible[x][y] = self._get_possible_choices(board, x, y)
            i += 1

        possible_bak = deepcopy(possible)
        i = 0
        while i < len(to_fill):
            x, y = to_fill[i]

            if len(possible[x][y]) == 0:
                possible[x][y] = deepcopy(possible_bak[x][y])
                board[x][y] = "."
                i -= 1
            else:
                board[x][y] = possible[x][y].pop()
                if self._is_valid(board, x, y):
                    i += 1
        print board

    @staticmethod
    def _get_possible_choices(board, x, y):
        all_choices = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        occurred = set()

        for c in board[x]:
            if c != '.':
                occurred.add(c)

        for row in board:
            c = row[y]
            if c != '.':
                occurred.add(c)

        x_area = x / 3
        y_area = y / 3
        area = [board[i][j] for i in range(0 + x_area * 3, 3 + x_area * 3) for j in
                range(0 + y_area * 3, 3 + y_area * 3)]
        for c in area:
            if c != '.':
                occurred.add(c)

        return all_choices.difference(occurred)

    @staticmethod
    def _is_valid(board, x, y):
        occurred = []
        for ch in board[x]:
            if ch != '.':
                if ch not in occurred:
                    occurred.append(ch)
                else:
                    return False
        occurred = []
        for row in board:
            if row[y] != '.':
                if row[y] not in occurred:
                    occurred.append(row[y])
                else:
                    return False

        occurred = []
        x_area = x / 3
        y_area = y / 3
        area = [board[i][j] for i in range(0 + x_area * 3, 3 + x_area * 3) for j in
                range(0 + y_area * 3, 3 + y_area * 3)]
        for c in area:
            if c != '.':
                if c not in occurred:
                    occurred.append(c)
                else:
                    return False

        return True

    @staticmethod
    def print_board(board):
        for row in board:
            print row


s = Solution()
s.solveSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)


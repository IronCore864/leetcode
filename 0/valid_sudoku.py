class Solution(object):
    def isValidSudoku(self, block):
        """
        :type board: List[str]
        :rtype: bool
        """
        for i in range(0, 9):
            row = [block[i][j] for j in range(0, 9) if block[i][j] != '.']
            arr_len = len(row)
            set_len = len(set(row))
            if arr_len != set_len:
                return False

            col = [block[j][i] for j in range(0, 9) if block[j][i] != '.']
            arr_len = len(col)
            set_len = len(set(col))
            if arr_len != set_len:
                return False

            x = i / 3
            y = i % 3
            small_block = [block[i][j] for i in range(0 + 3 * x, 0 + 3 * x + 3) for j in
                           range(0 + 3 * y, 0 + 3 * y + 3) if block[i][j] != '.']

            arr_len = len(small_block)
            set_len = len(set(small_block))
            if arr_len != set_len:
                return False

        return True


s = Solution()
print s.isValidSudoku([
    ".87654321",
    "2........",
    "3........",
    "4........",
    "5........",
    "6........",
    "7........",
    "8........",
    "9........"
])


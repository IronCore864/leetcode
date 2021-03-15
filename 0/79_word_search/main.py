from collections import Counter


class Solution:
    def search(self, board: list[list[str]], word: str, i: int, j: int) -> bool:
        # empty word, meaning all previous chars are already found
        if len(word) == 0:
            return True

        # out of bound, or char on the board isn't the same as the next char to search in the word, or board cell already visited
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0] or board[i][j] == '#':
            return False

        # current board cell matches the first char of the word
        # mark the current board cell as used temporarily
        # (instead of passing an extra map of visited cells)
        # (passing a map in theory increases the memory footprint but in reality doesn't increase much after test)
        tmp, board[i][j] = board[i][j], '#'
        # continue searching the up, down, left and right cells for the remaining part of the word
        res = self.search(board, word[1:],  i-1, j) or\
            self.search(board, word[1:],  i+1, j) or\
            self.search(board, word[1:],  i, j - 1) or\
            self.search(board, word[1:],  i, j+1)
        # reset the mark back
        board[i][j] = tmp
        return res

    def exist(self, board: list[list[str]], word: str) -> bool:
        # the word is longer than the size of the board
        if len(word) > len(board)*len(board[0]):
            return False

        # the board doesn't even have the requried characters to construct the word
        chars_in_word = Counter(word)
        chars_in_board = Counter([c for row in board for c in row])
        for c in chars_in_word:
            if chars_in_word[c] > chars_in_board[c]:
                return False

        # iterate all positions on the board, recursively search the next char in the word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, i, j):
                    return True

        # not found
        return False


if __name__ == '__main__':
    s = Solution()
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]

    word = 'ABCCED'
    assert s.exist(board, word) == True

    word = 'SEE'
    assert s.exist(board, word) == True

    word = 'ABCB'
    assert s.exist(board, word) == False

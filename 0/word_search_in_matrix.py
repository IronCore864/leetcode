class Solution(object):
    def dfs(self, board, taken, i, j, word):
        if word == "":
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j] or taken[i][j]:
            return False

        taken[i][j] = 1
        res = self.dfs(board, taken, i + 1, j, word[1:]) or self.dfs(board, taken, i - 1, j, word[1:]) \
              or self.dfs(board, taken, i, j + 1, word[1:]) or self.dfs(board, taken, i, j - 1, word[1:])
        taken[i][j] = 0

        return res

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        taken = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, taken, i, j, word):
                    return True
        return False


s = Solution()

board = ["baabab",
         "abaaaa",
         "abaaab",
         "ababba",
         "aabbab",
         "aabbba",
         "aabaab"]

print s.exist(board, "abaabbbaaaaababbbaaaaabbbaab")

from collections import defaultdict


class Node():
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        if not word:
            return

        current_node = self.root
        for w in word:
            current_node = current_node.children[w]
        current_node.is_word = True

    def search(self, word):
        current_node = self.root
        for w in word:
            current_node = current_node.children.get(w)
            if not current_node:
                return False
        return current_node.is_word


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.is_word:
            res.append(path)
            node.is_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp


s = Solution()
words = ["oath", "pea", "eat", "rain"]
board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
print(s.findWords(board, words))

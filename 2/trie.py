from collections import defaultdict


class Node():
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return

        current_node = self.root
        for w in word:
            current_node = current_node.children[w]
        current_node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for w in word:
            current_node = current_node.children.get(w)
            if not current_node:
                return False
        return current_node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for w in prefix:
            current_node = current_node.children.get(w)
            if not current_node:
                return False
        return True


obj = Trie()
print(obj.insert('abc'))
print(obj.search('abc'))
print(obj.search('ab'))
print(obj.insert('ab'))
print(obj.search('ab'))
print(obj.insert('ab'))
print(obj.search('ab'))

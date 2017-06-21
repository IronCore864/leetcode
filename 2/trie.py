class Node(object):
    def __init__(self, x):
        self.val = x
        self.keys = {}
        self.is_word = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return

        current_node = self.root
        for i in range(len(word)):
            key = word[i]
            prefix = word[:i + 1]
            if key not in current_node.keys:
                current_node.keys[key] = Node(prefix)
            current_node = current_node.keys[key]
        current_node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for ch in word:
            if ch in current_node.keys:
                current_node = current_node.keys[ch]
            else:
                return False
        return True if current_node.is_word else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for ch in prefix:
            if ch in current_node.keys:
                current_node = current_node.keys[ch]
            else:
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

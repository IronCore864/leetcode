class Node(object):
    def __init__(self, x):
        self.val = x
        self.keys = {}
        self.is_word = False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def addWord(self, word):
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

    def search_helper(self, word, i, current_node):
        # import pdb;pdb.set_trace()
        if i == len(word):
            return True if current_node.is_word else False

        if word[i] in current_node.keys:
            return self.search_helper(word, i + 1, current_node.keys[word[i]])
        elif word[i] == '.':
            for node in current_node.keys.values():
                if self.search_helper(word, i + 1, node):
                    return True
            return False
        else:
            return False

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.search_helper(word, 0, self.root)


obj = WordDictionary()

obj.addWord('test')
obj.addWord('track')
obj.addWord('truck')
obj.addWord('moock')

print(obj.search('te'))
print(obj.search('test'))
print(obj.search('tested'))
print(obj.search('tes.'))
print(obj.search('tr.ck'))
print(obj.search('...ck'))

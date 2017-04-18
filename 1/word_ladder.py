class Solution:
    def _get_next(self, word, wordDict):
        next_possible = set()
        for i in xrange(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in wordDict:
                    next_possible.add(next_word)
        return next_possible

    def ladderLength(self, beginWord, endWord, wordList):
        step = 1
        start = set([beginWord])
        wordDict = set(wordList)
        wordDict.discard(beginWord)

        while start:
            step += 1
            next_possible = set()
            for w in start:
                next_possible = next_possible.union(self._get_next(w, wordDict))
            wordDict -= next_possible
            if endWord in next_possible:
                return step
            start = next_possible
        return 0


s = Solution()
print s.ladderLength("hit",
                     "cog",
                     ["hot", "dot", "dog", "lot", "log", "cog"])

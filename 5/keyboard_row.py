class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')
        
        res = []
        for word in words:
            word_lower = set(word.lower())
            if word_lower.issubset(first_row) or word_lower.issubset(second_row) or word_lower.issubset(third_row):
                res.append(word)
        return res

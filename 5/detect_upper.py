class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word:
            return True
        
        if word.lower() == word:
            return True
        
        if word[0].lower() == word[0]:
            return False
        
        for ch in word[1:]:
            if ch.upper() == ch:
                return False
        return True
        

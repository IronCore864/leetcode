class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = [0] * 26
        for i in magazine:
            count[ord(i) - ord('a')] += 1

        for i in ransomNote:
            count[ord(i) - ord('a')] -= 1
            if count[ord(i) - ord('a')] < 0:
                return False
        return True

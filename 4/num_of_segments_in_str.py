class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = s.split(' ')
        res = [i for i in res if i]
        return len(res)

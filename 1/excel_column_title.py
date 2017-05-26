class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        a, b = divmod(n, 26)
        if b == 0:
            a -= 1
            b = 26

        if a <= 26:
            return (chr(64 + a) if a != 0 else '') + (chr(64 + b) if b != 0 else '')
        else:
            return self.convertToTitle(a) + (chr(64 + b) if b != 0 else '')


s = Solution()

for i in xrange(100000):
    print s.convertToTitle(i)

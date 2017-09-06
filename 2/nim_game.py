class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0


s = Solution()
for i in range(1, 30):
    print(s.canWinNim(i))

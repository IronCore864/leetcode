class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = []
        while True:
            c = [int(i) for i in str(n)]
            c.sort()
            if c in seen:
                return False
            n = 0
            for i in c:
                n += i * i
            if n == 1:
                return True
            seen.append(c)


s = Solution()
print(s.isHappy(11))

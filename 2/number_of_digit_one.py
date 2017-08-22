class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        q = n
        position = 1
        res = 0
        # n = xyzdabc
        # (1) xyz * 1000                     if d == 0
        # (2) xyz * 1000 + abc + 1           if d == 1
        # (3) xyz * 1000 + 1000              if d > 1

        while q > 0:
            d = q % 10

            q //= 10

            res += q * position

            if d == 1:
                res += n % position + 1
            elif d > 1:
                res += position

            position *= 10

        return res


s = Solution()
print(s.countDigitOne(123))

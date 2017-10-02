class Solution(object):
    def _int_to_hex(self, i):
        if i > 9:
            i -= 10
            i = chr(97 + i)
        return str(i)

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        if num < 0:
            num += 2 ** 32

        res = ''
        d, r = num, 0
        for i in range(1, 9):
            r = d % 16
            d = d // 16
            if r == 0 and d == 0:
                break
            res = self._int_to_hex(r) + res

        return res


s = Solution()
print(s.toHex(26))
print(s.toHex(-1))

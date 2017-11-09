class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num is None:
            return None

        if num == 0:
            return "0"

        sign = '-' if num < 0 else ''
        res = ''

        bit = 9
        r = abs(num)

        while bit >= 0:
            d = r // 7 ** bit
            r = r % 7 ** bit
            bit -= 1
            res += str(d)

        res = res.lstrip('0')
        return sign + res


s = Solution()
print(s.convertToBase7(100))
print(s.convertToBase7(-7))

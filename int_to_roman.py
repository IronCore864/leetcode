class Solution(object):
    def roman(self, num, i, v, x):
        r5 = num % 5
        d5 = num / 5
        if r5 < 4:
            res = i * r5
            if d5 == 0:
                return res
            elif d5 == 1:
                return v + res
        else:
            if d5 == 0:
                return i + v
            if d5 == 1:
                return i + x

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        tuhat = num / 1000
        sada = (num - tuhat * 1000) / 100
        kumme = (num - tuhat * 1000 - sada * 100) / 10
        uks = num % 10
        return self.roman(tuhat, "M", "v", "x") + self.roman(sada, "C", "D", "M") + self.roman(kumme, "X", "L", "C") + \
               self.roman(uks, "I", "V", "X")


s = Solution()
print s.intToRoman(1234)


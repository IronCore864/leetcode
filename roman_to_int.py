class Solution(object):
    def getVal(self, ch):
        return {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }.get(ch)

    def lessThan(self, ch1, ch2):
        return True if self.getVal(ch1) < self.getVal(ch2) else False

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        prev = None
        for ch in s[::-1]:
            if self.lessThan(ch, prev):
                sum -= self.getVal(ch)
            else:
                sum += self.getVal(ch)
            prev = ch
        return sum

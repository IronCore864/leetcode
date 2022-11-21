class Solution:
    def romanToInt(self, s: str) -> int:
        val = dict(zip(list("IVXLCDM"), [1, 5, 10, 50, 100, 500, 1000]))

        res = 0

        prev = 0
        for c in s[::-1]:
            v = val[c]
            res = res + v if v >= prev else res - v
            prev = val[c]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('LVIII'))
    print(s.romanToInt('MCMXCIV'))

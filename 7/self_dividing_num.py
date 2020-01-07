class Solution:
    def selfDividingNumbers(self, left, right):
        res = []
        for num in range(left, right + 1):
            num_str = str(num)
            r = True
            for s in num_str:
                if s == '0':
                    r = False
                    break
                if num % int(s) != 0:
                    r = False
                    break
            if r:
                res.append(num)
        return res

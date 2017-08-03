class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = s.replace(" ", "")
        n = len(s)

        stack = []
        num = 0
        sign = '+'

        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if not s[i].isdigit() or i == n - 1:
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    d = stack.pop()
                    r = d // num
                    if r < 0 and d % num != 0:
                        r += 1
                    stack.append(r)
                sign = s[i]
                num = 0
        res = 0
        for i in stack:
            res += i
        return res


s = Solution()
print(s.calculate(""))
print(s.calculate("123"))
print(s.calculate("3+2*2"))
print(s.calculate(" 3/2 "))
print(s.calculate("3+5 / 2"))
print(s.calculate("14/3*2"))
print(s.calculate("14-3/2"))
print(s.calculate("10000-1000/10+100*1"))

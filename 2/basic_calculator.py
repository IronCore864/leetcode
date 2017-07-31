class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")

        n = len(s)
        sign = 1
        result = 0
        stack = []

        i = 0
        while i < n:
            if s[i].isdigit():
                sum = int(s[i])
                while i + 1 < n and s[i + 1].isdigit():
                    sum = sum * 10 + int(s[i + 1])
                    i += 1
                result += sum * sign
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif s[i] == ')':
                result = result * stack.pop() + stack.pop()
            i += 1

        return result


s = Solution()
print(s.calculate("1"))

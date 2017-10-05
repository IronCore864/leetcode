class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num2) > len(num1):
            num1, num2 = num2, num1

        num1 = [int(i) for i in num1]

        carry = 0
        for i in range(-1, -len(num2) - 1, -1):
            num1[i] = num1[i] + int(num2[i]) + carry
            if num1[i] > 9:
                num1[i] -= 10
                carry = 1
            else:
                carry = 0
        for i in range(i - 1, -len(num1) - 1, -1):
            num1[i] += carry
            if num1[i] > 9:
                num1[i] -= 10
                carry = 1
            else:
                carry = 0
                break

        if carry:
            num1.insert(0, 1)
        return ''.join([str(i) for i in num1])


s = Solution()
print(s.addStrings("9", "99"))

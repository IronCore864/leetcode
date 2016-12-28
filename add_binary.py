class Solution(object):
    def _add_one_on_position(self, digits, n):
        digits = ['0'] + [i for i in digits]

        for i in range(len(digits) - n, -1, -1):
            if digits[i] == '0':
                digits[i] = '1'
                break
            else:
                digits[i] = '0'
        if digits[0] == '0':
            digits = digits[1:]
        return "".join(digits)

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.lstrip('0')
        b = b.lstrip('0')
        if len(b) > len(a):
            a, b = b, a
        if a == "" and b == "":
            return '0'

        if a == "":
            return b

        if b == "":
            return a

        for i in range(1, len(b) + 1):
            if b[-i] == '0':
                continue
            else:
                a = self._add_one_on_position(a, i)

        return a


s = Solution()
print s.addBinary("11", "1")
print s.addBinary("100", "110010")

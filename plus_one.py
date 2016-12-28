class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]

        digits = [0] + digits
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] -= 10
            else:
                break
        if digits[0] == 0:
            digits = digits[1:]

        return digits


s = Solution()
print s.plusOne([9, 0, 9])
print s.plusOne([9, 9, 9])
print s.plusOne([1, 2, 3, 4, 5])

class Solution:
    def selfDividingNumbers(self, left, right):
        return [num for num in range(left, right + 1) if all(int(i) != 0 and num % int(i) == 0 for i in str(num))]

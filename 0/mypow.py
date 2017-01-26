class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)


s = Solution()
print s.myPow(2, 0)
print s.myPow(2, -1)
print s.myPow(2, -2)
print s.myPow(2, 1)
print s.myPow(2, 2)
print s.myPow(2, 32)
print s.myPow(2.123, 3)
print s.myPow(2.123, -3)
print s.myPow(0.00001, 2147483647)


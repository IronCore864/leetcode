class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        r = 1
        step = 3
        num = 3
        while n > num:
            step += 2
            num += step
            r += 1
        return r


s = Solution()
for i in range(1, 100):
    print(i, s.bulbSwitch(i))

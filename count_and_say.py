class Solution(object):
    def get_next(self, num):
        prev = ''
        count = 0
        res = ""
        for ch in str(num):
            if ch != prev:
                if count != 0:
                    res = res + str(count) + str(prev)
                prev = ch
                count = 1
            else:
                count += 1
        res = res + str(count) + str(prev)
        return res

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = 1
        count = 1
        while count < n:
            res = self.get_next(res)
            count += 1
        return str(res)


s = Solution()
for i in range(1, 10):
    print s.countAndSay(i)


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum([1 for i in "{0:b}".format(x ^ y) if i == '1'])


s = Solution()
print(s.hammingDistance(1, 4))

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        b = '{0:032b}'.format(n)
        for i in b:
            if i == '1':
                res += 1
        return res

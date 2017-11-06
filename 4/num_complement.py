class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(['0' if i == '1' else '1' for i in "{0:b}".format(num)]), 2)

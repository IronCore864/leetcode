class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == '-':
            signal = '-'
            s = s[1:]
        else:
            signal = ''
        res_str = signal+s[-1:-len(s)-1:-1]
        reversedInt = int(res_str)
        return reversedInt if (-1)*2**31<reversedInt<(2**31-1) else 0

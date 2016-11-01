class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is None:
            return 0

        str = str.strip()

        if str == '':
            return 0

        if len(str) == 1:
            if str.isdigit():
                return int(str)
            else:
                return 0

        valid_chars = ['0','1','2','3','4','5','6','7','8','9','-','+']

        if str[0] == '-':
            minus = True
            str = str[1:]
        elif str[0] == '+':
            minus = False
            str = str[1:]
        elif str[0] not in valid_chars:
            return 0
        else:
            minus = False

        l = 0
        for c in str:
            if c in ['0','1','2','3','4','5','6','7','8','9','-','+']:
                l += 1
            else:
                break
        str = str[0:l]

        if not str.isdigit():
            return 0
        else:
            val = int(str)
        if minus:
            val*=-1

        if -1*2**31<=val<2**31-1:
            return val
        elif val>=2**31-1:
            return 2**31-1
        elif val<-1*2**31:
            return -1*2**31
        else:
            return 0

s = Solution()
print s.myAtoi("  -0012a42")
#print s.myAtoi("-123")

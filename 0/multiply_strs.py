class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        pos = [0 for _ in range(m + n)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1;
                sum = mul + pos[p2];
                pos[p1] += sum / 10;
                pos[p2] = (sum) % 10;

        started = False
        res = ''
        for ch in pos:
            if ch == 0 and started is False:
                continue
            if ch != 0 and started is False:
                started = True
            res += str(ch)
        return res if res != '' else '0'


s = Solution()
print s.multiply('123', '45')


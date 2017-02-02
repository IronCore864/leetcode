class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in xrange(1, 4):
            for j in xrange(i + 1, i + 4):
                for k in xrange(j + 1, j + 4):
                    a, b, c, d = s[0:i], s[i:j], s[j:k], s[k:]
                    if b == '' or c == '' or d == '':
                        continue
                    if int(a) > 255 or int(b) > 255 or int(c) > 255 or int(d) > 255 or len(d) == 0:
                        continue
                    if len(a) > 1 and a[0] == '0':
                        continue
                    if len(b) > 1 and b[0] == '0':
                        continue
                    if len(c) > 1 and c[0] == '0':
                        continue
                    if len(d) > 1 and d[0] == '0':
                        continue
                    res.append(".".join([a, b, c, d]))
        return res


s = Solution()
res = s.restoreIpAddresses('0000')
for r in res:
    print r

class Solution:
    def subsets(self, S):
        res = [[]]
        S.sort()
        for i in xrange(len(S)):
            for j in xrange(0, len(res)):
                res.append(res[j] + [S[i]])
        return res

s = Solution()
res = s.subsets([1, 2, 3, 4, 5])

for row in res:
    print row

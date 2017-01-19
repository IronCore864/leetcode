class Solution:
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            # if S[i] is same to S[i - 1], then it needn't to be added to all of the subset,
            # just add it to the last l subsets which are created by adding S[i - 1]
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res


s = Solution()
res = s.subsetsWithDup([1, 2, 2])

for row in res:
    print row

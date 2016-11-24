class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, candidates, target, path, res):
        if target == 0 and path and path not in res:
            res.append(path)
        for i in range(len(candidates)):
            if candidates[i] > target: break
            self.dfs(candidates[i + 1:], target - candidates[i], path + [candidates[i]], res)
        return res


s = Solution()
print s.combinationSum2(
    [23, 29, 8, 24, 5, 7, 25, 29, 18, 18, 32, 29, 30, 5, 9, 23, 27, 15, 28, 32, 11, 24, 11, 29, 12, 32, 5, 7, 31, 16, 7,
     19, 10, 33, 8, 10, 5, 21, 26, 18, 26, 23, 5, 21, 24, 31, 31, 8, 11, 16, 5, 17, 5, 33, 34, 12, 31, 26, 7, 27], 22)


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, 10)]
        if k > 9 or sum(nums[:k]) > n or sum(nums[-k:]) < n:
            return []
        res = []
        self._helper(k, n, 1, [], res)
        return res

    def _helper(self, k, n, curr, arr, res):
        if len(arr) == k:
            if sum(arr) == n:
                res.append(list(arr))
            return

        if len(arr) > k or curr > 9:
            return

        for i in range(curr, 10):
            arr.append(i)
            self._helper(k, n, i + 1, arr, res)
            arr.pop()


s = Solution()
print(s.combinationSum3(2, 7))

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]  # prefix sum
            res += d.get(sums-k, 0)
            d[sums] = d.get(sums, 0) + 1

        return res

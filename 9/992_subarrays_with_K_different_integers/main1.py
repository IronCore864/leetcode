from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # since len(nums) <= 10**4
        # we can't do an O(n**2) algorithm
        # because 10**8 will probably time out
        
        n = len(nums)
        res = 0
        for i in range(0, n):
            for j in range(i + 1, n + 1):
                if len(set(nums[i:j])) == k:
                    res += 1
        return res

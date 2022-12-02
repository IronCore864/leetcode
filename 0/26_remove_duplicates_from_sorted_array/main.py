from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        prev = nums[0]
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] == prev:
                continue

            nums[cur] = nums[i]
            prev = nums[i]
            cur += 1

        return cur

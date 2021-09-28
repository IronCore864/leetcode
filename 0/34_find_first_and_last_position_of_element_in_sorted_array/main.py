from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return -1, -1

        res1, res2 = -1, -1

        lo, hi = 0, len(nums)-1
        while lo <= hi:
            a = (lo + hi) // 2
            if target <= nums[a]:
                hi = a - 1
            elif nums[a] < target:
                lo = a + 1
        res1 = -1 if lo >= len(nums) or nums[lo] != target else lo

        lo, hi = 0, len(nums)-1
        while lo <= hi:
            b = (lo + hi) // 2
            if target < nums[b]:
                hi = b - 1
            elif nums[b] <= target:
                lo = b + 1
        res2 = -1 if hi < 0 or nums[hi] != target else hi
        return res1, res2


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(s.searchRange([], 0))

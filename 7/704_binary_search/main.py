from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            if nums[mid] > target:
                hi = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))
    print(s.search([-1, 0, 3, 5, 9, 12], 2))

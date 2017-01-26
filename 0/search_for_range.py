class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        found = -1
        while lo <= hi:
            mid = (lo + hi) / 2;
            if nums[mid] == target:
                found = mid
                break
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        if found == -1:
            return -1, -1
        else:
            left = found
            right = found
            while left - 1 >= 0 and nums[left - 1] == nums[found]:
                left -= 1
            while right + 1 < len(nums) and nums[right + 1] == nums[found]:
                right += 1
            return left, right


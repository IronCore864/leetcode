class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                pass
            elif nums[i] > target:
                return i


s = Solution()
print s.searchInsert([1, 3, 5, 6], 5)
print s.searchInsert([1, 3, 5, 6], 2)
print s.searchInsert([1, 3, 5, 6], 7)
print s.searchInsert([1, 3, 5, 6], 0)


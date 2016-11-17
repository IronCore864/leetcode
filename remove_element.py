class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        parse = 0
        store = 0
        while parse < len(nums):
            if nums[parse] != val:
                nums[store] = nums[parse]
                store += 1
                parse += 1
            else:
                parse += 1
        return store


s = Solution()
print s.removeElement([3, 2, 2, 3], 3)


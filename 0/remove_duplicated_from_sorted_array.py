class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 0:
            return 0

        store_pos = 1
        parse_pos = 1
        while parse_pos < len(nums):
            if nums[parse_pos] != nums[store_pos - 1]:
                nums[store_pos] = nums[parse_pos]
                parse_pos += 1
                store_pos += 1
            else:
                parse_pos += 1
        return store_pos


s = Solution()
print s.removeDuplicates([1, 1])


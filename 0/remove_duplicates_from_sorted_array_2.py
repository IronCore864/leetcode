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
        has_two_already = False
        while parse_pos < len(nums):
            if nums[parse_pos] == nums[store_pos - 1]:
                if not has_two_already:
                    nums[store_pos] = nums[parse_pos]
                    has_two_already = True
                    store_pos += 1
            else:
                has_two_already = False
                nums[store_pos] = nums[parse_pos]
                store_pos += 1
            parse_pos += 1
        print nums
        return store_pos


s = Solution()
print s.removeDuplicates([1, 1, 1, 2, 2, 3])
print s.removeDuplicates([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5])

class Solution(object):
    def firstMissingPositive(self, nums):
        i=0
        len_num = len(nums)
        # if number is between [1, len_num], move it to index number-1
        # ignore negative, 0, larger than len_num, and the same as before numbers
        while i < len_num:
            num = nums[i]
            if num != i + 1 and 1 <= num <= len_num and num != nums[num - 1]:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
            else:
                i += 1

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        else:
            return len_num + 1



s = Solution()
print s.firstMissingPositive([3, 4, -1, 1])


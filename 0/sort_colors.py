class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_idx += 1
            else:
                break

        two_idx = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                two_idx -= 1
            else:
                break

        i = zero_idx
        while i <= two_idx:
            if nums[i] == 1:
                i += 1
                continue
            if nums[i] == 0:
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                if i == zero_idx:
                    i += 1
                zero_idx += 1
                continue
            if nums[i] == 2:
                nums[i], nums[two_idx] = nums[two_idx], nums[i]
                two_idx -= 1
                continue
        return nums


s = Solution()
print s.sortColors([1, 0, 0, 2, 0, 1, 0, 2, 2, 1, 0])

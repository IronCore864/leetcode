class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find the first index from the right to left, so that nums[index]>nums[index+1]
        index = -1
        for i in range(len(nums) - 2, 0, -1):
            if nums[i - 1] < nums[i]:
                index = i - 1
                break

        # if such index does not exist, it means the array is ordered by desc
        # in this case, the next permutation is nums.sort() which is ordered by asc
        if index == -1:
            nums.sort()
            return

        min_nbr_idx_gt_first_asc_idx_bkwd = len(nums)
        min_nbr_gt_first_asc_bkwd = 2 ** 31 - 1

        # from nums[index+1:] find the smallest number which is larger than nums[i]
        for i in range(index + 1, len(nums)):
            if nums[i] > nums[index] and nums[i] < min_nbr_gt_first_asc_bkwd:
                min_nbr_gt_first_asc_bkwd = nums[i]
                min_nbr_idx_gt_first_asc_idx_bkwd = i
        # swap num[index] and the newly found number
        nums[index], nums[min_nbr_idx_gt_first_asc_idx_bkwd] = nums[min_nbr_idx_gt_first_asc_idx_bkwd], \
                                                               nums[index]
        # sort nums[index+1:] asc
        nums[index + 1:] = sorted(nums[index + 1:])
        return


s = Solution()

nums = [1, 2, 3]
s.nextPermutation(nums)
print nums

nums = [3, 2, 1]
s.nextPermutation(nums)
print nums

nums = [5, 7, 9, 4, 1]
s.nextPermutation(nums)
print nums


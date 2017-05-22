class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            m = i + (j - i) / 2
            if nums[m] > nums[j]:
                i = m + 1
            elif nums[m] < nums[j]:
                j = m
            else:
                j -= 1
        return nums[i]


s = Solution()
print s.findMin([3, 3, 1, 3])

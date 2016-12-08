class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        leftmost = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= leftmost:
                leftmost = i
        return True if leftmost == 0 else False


s = Solution()
print s.canJump([2, 3, 1, 1, 4])
print s.canJump([3, 2, 1, 0, 4])


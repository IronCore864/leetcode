class Solution(object):
    def _reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        n = len(nums)
        k = k % n
        if k == 0:
            return
        self._reverse(nums, 0, len(nums) - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, len(nums) - 1)

        return nums


s = Solution()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))

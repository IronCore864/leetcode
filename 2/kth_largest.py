class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.partition(nums, 0, len(nums) - 1, k)

    def partition(self, nums, left, right, k):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]

        if i + 1 == k:
            return nums[i]
        elif i + 1 > k:
            return self.partition(nums, left, i - 1, k)
        else:
            return self.partition(nums, i, right, k)


s = Solution()
a = [6, 2, 5, 3, 1, 4]
for i in range(1, len(a) + 1):
    print(s.findKthLargest(a, i))

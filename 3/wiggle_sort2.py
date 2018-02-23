from random import randint


class Solution:
    def findKthLargest(self, nums, k):
        return self.partition(nums, 0, len(nums) - 1, k)

    def partition(self, nums, left, right, k):
        r = randint(left, right)
        nums[r], nums[right] = nums[right], nums[r]

        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] >= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]

        if i + 1 == k:
            return nums[i]
        elif i + 1 > k:
            return self.partition(nums, left, i - 1, k)
        else:
            return self.partition(nums, i, right, k)

    def newIndex(self, i, n):
        return (1 + 2 * i) % (n | 1)

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        m = n // 2 if n % 2 == 0 else n // 2 + 1
        median = self.findKthLargest(nums, m)

        left, i, right = 0, 0, n - 1

        while i <= right:

            if nums[self.newIndex(i, n)] > median:
                nums[self.newIndex(left, n)], nums[self.newIndex(i, n)] = nums[self.newIndex(i, n)], nums[
                    self.newIndex(left, n)]
                left += 1
                i += 1
            elif nums[self.newIndex(i, n)] < median:
                nums[self.newIndex(right, n)], nums[self.newIndex(i, n)] = nums[self.newIndex(i, n)], nums[
                    self.newIndex(right, n)]
                right -= 1
            else:
                i += 1

# in fact using python, with extreme corner cases, using sort is faster

s = Solution()
nums = [1, 3, 2, 2, 3, 1]
s.wiggleSort(nums)
print(nums)

class Solution:
    # since we can consider the left border and the right border of the list as -inf
    # it's guaranteed that the peak exists
    # all we need to do is to find the end of an increasing slope where nums[i] > nums[i+1]
    # hence binary search works here
    # explanation in pictures see here: https://leetcode.com/problems/find-peak-element/solution/
    def findPeakElement(self, nums: list[int]) -> int:
        l = 0
        r = len(nums)-1

        while l != r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1

        return l


if __name__ == '__main__':
    s = Solution()
    assert s.findPeakElement([1, 2, 3, 1]) == 2
    assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5

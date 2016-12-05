"""
This problem was discussed by Jon Bentley (Sep. 1984 Vol. 27 No. 9 Communications of the ACM P885)

The paragraph below was copied from his paper (with a little modifications)

Algorithm that operates on arrays:

it starts at the left end from the first element, and scans through to the right end,
keeping track of the maximum sum subvector seen so far.

The maximum is initially A[0]. Suppose we've solved the problem for A[1 .. i - 1]; how can we extend that to A[1 .. i]?
The maximum sum in the first i elements is either the maximum sum in the first i - 1 elements (which we'll call MaxSoFar),
or it is that of a subvector that ends in position i (which we'll call MaxEndingHere).
MaxEndingHere is either A[i] plus the previous MaxEndingHere, or just A[i], whichever is larger.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_so_far = nums[0]
        max_ending_here = nums[0]

        for num in nums[1:]:
            max_ending_here = max(max_ending_here + num, num)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


s = Solution()
print s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])


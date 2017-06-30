from heapq import nlargest, heapify


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapify(nums)
        return nlargest(k, nums)[-1]


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))

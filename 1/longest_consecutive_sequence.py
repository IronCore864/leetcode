class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        result = 0
        for x in nums:
            if x - 1 not in nums:
                l = 1
                y = x + 1
                while y in nums:
                    y += 1
                    l += 1
                result = max(result, l)
        return result


s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])
print s.longestConsecutive([1, 2, 3])

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        n = len(nums)
        if n == 1:
            return [str(nums[0])]

        i = 0
        res = []
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if start != nums[i]:
                res.append(str(start) + "->" + str(nums[i]))
            else:
                res.append(str(start))
            i += 1

        return res


s = Solution()
print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
# # ["0->2","4->5","7"]
print(s.summaryRanges([1]))
print(s.summaryRanges([1, 2, 3, 4, 5]))

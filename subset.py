class Solution(object):
    def combine(self, nums, k):
        if k == 1:
            return [[i] for i in nums]
        elif k == len(nums):
            return [[i for i in nums]]
        else:
            rs = []
            rs += self.combine(nums[:-1], k)
            part = self.combine(nums[:-1], k - 1)
            for ls in part:
                ls.append(nums[-1])
            rs += part
            return rs

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        for i in range(1, len(nums) + 1):
            res += self.combine(nums, i)
        return res


s = Solution()
res = s.subsets([1, 2, 3, 4, 5])

for row in res:
    print row

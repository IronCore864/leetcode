class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            new = []
            for each in res:
                for i in range(0, len(each) + 1):
                    new.append(each[:i] + [num] + each[i:])
            res = new
        return res


s = Solution()
print s.permute([1, 2, 3])
res = s.permute([1, 2, 3, 4, 5, 6, 7, 8, 9])
print len(res)


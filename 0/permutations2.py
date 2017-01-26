class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            new = []
            for each in res:
                for i in range(0, len(each) + 1):
                    tmp = each[:i] + [num] + each[i:]
                    if tmp not in new:
                        new.append(tmp)
            res = new
        return res


s = Solution()
print s.permuteUnique([1, 1, 2])
res = s.permuteUnique([1, 1, 2, 2, 3, 4, 5, 6])
print len(res)


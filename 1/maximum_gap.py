import math


class Solution:
    def maximumGap(self, nums):
        if not nums:
            return 0

        new_nums = set()
        a, b = nums[0], nums[0]
        for n in nums:
            if n > b:
                b = n
            if n < a:
                a = n
            new_nums.add(n)
        nums = list(new_nums)

        if len(nums) < 2 or a == b:
            return 0

        size = int(math.ceil((b - a) / (len(nums) - 1)))

        buckets = [[None, None] for _ in xrange((b - a) / size + 1)]
        for n in nums:
            b = buckets[(n - a) / size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)

        buckets = [b for b in buckets if b[0] is not None]

        res = 0
        for i in xrange(1, len(buckets)):
            if buckets[i][0] - buckets[i - 1][1] > res:
                res = buckets[i][0] - buckets[i - 1][1]
        return res


s = Solution()
print s.maximumGap([1, 3, 100])

class Solution:
    def findShortestSubArray(self, nums):
        first, count, res, degree = {}, {}, 0, 0
        for i, num in enumerate(nums):
            first.setdefault(num, i)
            count[num] = count.get(num, 0) + 1
            if count[num] > degree:
                degree = count[num]
                res = i - first[num] + 1
            elif count[num] == degree:
                res = min(res, i - first[num] + 1)
        return res


s = Solution()
print(s.findShortestSubArray([]))
print(s.findShortestSubArray([1]))
print(s.findShortestSubArray([1, 2, 2, 3, 1]))
print(s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))

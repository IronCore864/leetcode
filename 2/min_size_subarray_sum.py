class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = end = 0
        n = len(nums)
        current_sum = 0
        res = 2 ** 31 - 1

        while start < n and end <= n:
            if current_sum < s:
                if n == end:
                    break
                else:
                    current_sum += nums[end]
                    end += 1
            else:
                res = min(res, end - start)
                current_sum -= nums[start]
                start += 1

        return 0 if res == 2 ** 31 - 1 else res


s = Solution()
print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Constraints:
            1 <= nums.length <= 100
            0 <= nums[i] <= 400
        (Even O(n**2) could work.)
        """

        # for each house, either rob it, or not

        # if the current house (i) is robbed, the previous one (i-1) can't be robbed
        # the maximum amount equals to what you can get till house (i-2) plus house (i)

        # if the current hosue (i) is not robbed, the previous one (i-1) can be robbed
        # the max equas to what you can get till house (i-1)

        # we use an array amount to store the max amount,
        # amount[i] means the maximum amount you can get from house 0 to house i (inclusive)

        # i.e.,
        # amount[i] = max(
        #   nums[i] + amount[i-2], # take house[i]
        #   amount[i-1] # don't take house[i]
        # )

        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]

    def rob_reduce_memory_footprint(self, nums: List[int]) -> int:
        """
        since amount[i] = max(nums[i] + amount[i-2], nums[i-1])
        we only need amount_previous, and amount_pre_previous
        """
        n = len(nums)

        if n == 1:
            return nums[0]

        amount_pre_previous = nums[0]
        amount_previous = max(nums[0], nums[1])

        res = amount_previous

        for i in range(2, n):
            res = max(amount_pre_previous + nums[i], amount_previous)
            amount_pre_previous, amount_previous = amount_previous, res

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([[2, 7, 9, 3, 1]]))

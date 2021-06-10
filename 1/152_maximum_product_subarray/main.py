from sys import maxsize


class Solution:
    def maxProduct_bruteforce(self, nums: list[int]) -> int:
        n = len(nums)
        res = -maxsize

        for i in range(n):
            for j in range(i+1, n+1):
                product = 1
                for num in nums[i:j]:
                    product *= num
                res = max(res, product)

        return res

    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]

        n = len(nums)
        # imax/imin stores the max/min product of
        # subarray that ends with the current number nums[i]

        imax = res
        imin = res
        for i in range(1, n):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the imax and imin by swapping them
            if nums[i] < 0:
                imax, imin = imin, imax

            # max and min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])

            # the newly computed max value is a candidate for our global result
            res = max(res, imax)

        return res


if __name__ == '__main__':
    s = Solution()
    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([-2, 0, -1]) == 0

class Solution(object):
    def splitArray(self, nums, m):
        def is_valid(nums, m, largest_sum):
            """
            "valid" means it's possible to cut the array into m chunks so that the max sum of each chunk is less than the largest_sum
            """
            cut, cur_sum = 0, 0
            for x in nums:
                cur_sum += x
                if cur_sum > largest_sum:
                    cut += 1
                    cur_sum = x
            # if we can cut the array in less than m chunks and the sum of each chunk is less than largest_sum, it's valid
            return cut + 1 <= m

        # we do a binary search on the minimum largest sum

        # the max possible largest sum is sum(nums): no cut (or into 1 chunk)
        hi = sum(nums)

        # the min possible largest sum is max(nums): cut into len(nums) chunks
        lo = max(nums)

        res = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if is_valid(nums, m, mid):
                # if valid, we could try to decrease the minimum largest sum
                res = mid
                hi = mid - 1
            else:
                # if not valid, we must increase the minimum largest sum
                lo = mid + 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.splitArray([7, 2, 5, 10, 8], 2))

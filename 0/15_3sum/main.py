class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n < 3:
            return []

        nums.sort()
        res = []

        for i in range(n-2):
            # remove duplicated results
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # bi-directional two-sum
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    # remove duplicated results
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))

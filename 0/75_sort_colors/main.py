class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = 0
        two = n-1

        for i in range(n):
            while nums[i] == 2 and i < two:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            while nums[i] == 0 and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

        # for testing purpose; this problem doesn't require return value
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    assert s.sortColors(nums) == [0, 0, 1, 1, 2, 2]

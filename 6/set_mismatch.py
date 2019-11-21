class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        repeat = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                repeat = nums[i]
                break
        missing = (1+len(nums))*len(nums)//2 - sum(nums) + repeat
        return [repeat, missing]

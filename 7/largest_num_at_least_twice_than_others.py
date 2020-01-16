class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, second_largest, largest_index = -1, -1, -1
        for i in range(len(nums)):
            if nums[i]>largest:
                second_largest = largest
                largest = nums[i]
                largest_index = i
            elif largest>nums[i]>second_largest:
                second_largest=nums[i]
        return largest_index if largest>=2*second_largest else -1

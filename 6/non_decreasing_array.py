class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        already_changed = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if already_changed:
                    return False
                already_changed = True
                if i == 0:
                    nums[i] = nums[i+1]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                else:
                    nums[i+1] = nums[i]
        return True

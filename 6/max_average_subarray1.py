class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pre_sum = sum(nums[0:k])
        max_sum = pre_sum

        for i in range(len(nums)-k):
            next_sum = pre_sum - nums[i] + nums[i + k]
            if next_sum > max_sum:
                max_sum = next_sum
            pre_sum = next_sum

        return max_sum/k
        

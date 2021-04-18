from bisect import bisect_left, bisect_right, insort


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # sums[i] means: nums[0] + nums[1] + ... + nums[i-1], not including nums[i]
        # or to say, 
        # sums[i] == sum(nums[:i])
       
        # example:

        # nums = [1, 2, 3, 4, 5]
        # sums = [0, 1, 3, 6, 10, 15]
        # sums[0] == sum(nums[:0]), where num[0] is not inclusive, hence, sums[0] == 0
        # so we initiate prefix_sums as [0]
        
        sums = [0]

        # stores the result, i.e., the count where lower <= sum(nums[i:j]) <= upper
        res = 0 
        
        # we are trying to find all possible i's and j's, so that sum(nums[i:j]) >=lower, and sum(nums[i:j]) <= upper
        # since sum(nums[i:j]) = sums[j] - sums[i]
        # this means, we want i's and j's so that
        # sums[j] - sums[i] >= lower
        # and
        # sums[j] - sums[i] <= upper
        
        sums_j = 0
        
        # iterate over all the numbers
        for num in nums:
            # sum from zero till the curent number
            sums_j += num
            
            # calculating possible solutions where lower <= sum[j] - sum[i] <= upper
        
            # as long as sums[i] <= sums[j] - lower, sum(nums[i:j]) will be lager than the lower bound
            # a means the number of i's where sums[j] - sums[i] >= lower
            a = bisect_right(sums, sums_j - lower)
            # as long as sums[i] < sums[j] - upper, sum(nums[i:j]) will NOT be smaller than upper
            # b means the number if i's where sums[j] - sums[i] NOT smaller than upper
            b = bisect_left(sums, sums_j - upper)
        
            possible_i = a - b
          
            res += possible_i
            
            # add the current prefix sums
            insort(sums, sums_j)
        
        return res

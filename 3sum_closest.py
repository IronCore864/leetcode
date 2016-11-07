class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # if there is only one element in the nums array, return it
        if len(nums) == 1:
            return nums[0]

        # if there are two elements in the nums array, the closest sum to the target is nums[0], nums[1],
        # or nums[0] + nums[1]
        if len(nums) == 2:
            num0 = abs(nums[0] - target)
            num1 = abs(nums[1] - target)
            num01 = abs(nums[0] + nums[1] - target)
            if num0 < num1 and num0 < num01:
                return nums[0]
            if num1 < num0 and num1 < num01:
                return nums[1]
            if num01 < num0 and num01 - num1:
                return nums[0] + nums[1]

        # if there are more than two elements in the nums array, use i, j, k as three pointers
        # sort first
        nums = sorted(nums)
        min_closest = 2 ** 31 - 1 if target < 0 else -2 ** 31
        # iterate i from 0 to len(nums)-2
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            closest = 2 ** 31 - 1 if target < 0 else -2 ** 31
            # for the remaining part of the nums array, iterate from the beginning and end and find the closest sum
            while j != k:
                if nums[i] + nums[j] + nums[k] == target:
                    return target

                if not closest:
                    closest = nums[i] + nums[j] + nums[k]
                else:
                    if abs(nums[i] + nums[j] + nums[k] - target) < abs(closest - target):
                        closest = nums[i] + nums[j] + nums[k]

                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
            min_closest = closest if abs(closest - target) < abs(min_closest - target) else min_closest
        return min_closest


s = Solution()
print s.threeSumClosest([-1, 2, 1, -4], 1)


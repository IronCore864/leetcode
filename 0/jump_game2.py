class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step_count = 0
        last_jump_max = 0
        current_jump_max = 0
        for i in range(0, len(nums) - 1):
            current_jump_max = max(current_jump_max, i + nums[i])
            if current_jump_max >= len(nums) - 1:
                return step_count + 1

            if i == last_jump_max:
                step_count += 1
                last_jump_max = current_jump_max
        return step_count

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums = sorted(nums)
        res = []
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                k = j + 1
                l = len(nums) - 1
                while k != l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        if not [nums[i], nums[j], nums[k], nums[l]] in res:
                            res.append([nums[i], nums[j], nums[k], nums[l]])
                    if nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l -= 1
                    else:
                        k += 1
        return res


s = Solution()
print s.fourSum(
    [-491, -477, -450, -436, -431, -410, -402, -402, -391, -381, -380, -377, -355, -346, -344, -325, -320, -318, -290,
     -286, -278, -278, -272, -261, -261, -259, -235, -234, -232, -220, -212, -206, -201, -196, -191, -186, -173, -164,
     -158, -133, -120, -98, -91, -87, -82, -73, -62, -55, -27, 0, 14, 19, 23, 37, 48, 52, 53, 53, 57, 83, 85, 106, 161,
     170, 174, 183, 188, 191, 197, 211, 212, 222, 231, 243, 250, 274, 284, 302, 313, 319, 332, 338, 356, 358, 369, 374,
     396, 406, 416, 420, 425, 440, 441, 443, 469, 471, 496], -2402)
print s.fourSum([1, 0, -1, 0, -2, 2], 0)


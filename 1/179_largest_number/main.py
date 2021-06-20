class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        nums.sort(key=LargerNumKey)
        return '0' if nums[0] == '0' else ''.join(nums)

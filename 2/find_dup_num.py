class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]

        fast = 0
        while fast != slow:
            fast, slow = nums[fast], nums[slow]

        return slow

# http://keithschwarz.com/interesting/code/?dir=find-duplicate
# cycle detection
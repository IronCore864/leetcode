class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = None
        count = 0
        for n in nums:
            if res is None:
                res = n
                count = 1
            elif res == n:
                count += 1
            elif res !=n:
                count -= 1
                if count == 0:
                    res = None
        return res
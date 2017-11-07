class Solution(object):
    def nextGreaterElement(self, find_nums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        next_greater_num = {}
        stack = []

        for num in nums:
            while stack and stack[-1] < num:
                next_greater_num[stack.pop()] = num
            stack.append(num)

        res = []
        for num in find_nums:
            res.append(next_greater_num.get(num, -1))
            
        return res

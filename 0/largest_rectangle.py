class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # save height index
        stack = []
        res = 0
        heights.append(0)

        for i in xrange(len(heights)):
            # if stack is empty, push current height index into it
            if len(stack) == 0:
                stack.append(i)
            # if current height is bigger than the top of the stack, push current height index into stack
            elif heights[stack[-1]] <= heights[i]:
                stack.append(i)
            # if current height is smaller than the top of the stack
            else:
                # pop one from the stack, and use it as height and left column, calculate the area from this col to i-1
                while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    right = i
                    left = -1 if len(stack) == 0 else stack[-1]
                    w = right - left - 1
                    res = max(res, h * w)
                stack.append(i)
        return res


s = Solution()
print s.largestRectangleArea([2, 1, 5, 6, 2, 3])
print s.largestRectangleArea([1])

class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        res = 0
        heights.append(0)
        for i in xrange(len(heights)):
            if len(stack) == 0:
                stack.append(i)
            elif heights[stack[-1]] <= heights[i]:
                stack.append(i)
            else:
                while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    right = i
                    left = -1 if len(stack) == 0 else stack[-1]
                    w = right - left - 1
                    res = max(res, h * w)
                stack.append(i)
        return res

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        heights = [int(i) for i in matrix[0]]
        result = self.largestRectangleArea(heights)

        for row in matrix[1:]:
            for i in xrange(len(row)):
                if int(row[i]) == 1:
                    heights[i] += 1
                else:
                    heights[i] = 0
            result = max(result, self.largestRectangleArea(heights))
        return result


s = Solution()
print s.maximalRectangle([
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0],
])

print s.maximalRectangle([
    "10100",
    "10111",
    "11111",
    "10010"
])

print s.maximalRectangle([
    "1",
])

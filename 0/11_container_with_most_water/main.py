class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)

        # starting from two ends, because longer width container might hold more water
        left = 0
        right = n - 1

        res = 0

        while left < right:
            # calculate the water volume
            res = max(res, (right-left)*min(height[left], height[right]))

            # move the shorter wall inward
            # the water is limited by the shorter wall
            # if you move the taller wall, even if the next is even taller, the total volume of the water can't increase,
            if height[left] < height[right]:
                left += 1
                # until a taller one is found
                # this reduces some unnecessary calculations
                while height[left] <= height[left-1] and left < n:
                    left += 1
            else:
                right -= 1
                while height[right] <= height[right+1] and right > 0:

                    right -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    assert s.maxArea([1, 1]) == 1
    assert s.maxArea([4, 3, 2, 1, 4]) == 16
    assert s.maxArea([1, 2, 1]) == 2
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

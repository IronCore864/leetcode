class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)

        # starting from two ends, because longer width container might hold more water
        i = 0
        j = n - 1

        res = 0

        while i < j:
            # calculate the water volume
            res = max(res, (j-i)*min(height[i], height[j]))

            # move the shorter wall to the next
            # this is because the water is limited by the shorter wall
            # if you move the taller wall, even if the next is even taller, the total volume of the water can't increase,
            # because the width reduces and the highest water level is decided by the shorter wall
            if height[i] < height[j]:
                i += 1
                # until a taller one is found
                # this reduces some unnecessary calculations
                while height[i] <= height[i-1] and i < n:
                    i += 1
            else:
                j -= 1
                while height[j] <= height[j+1] and j > 0:
                    j -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.maxArea([1, 1]) == 1
    assert s.maxArea([4, 3, 2, 1, 4]) == 16
    assert s.maxArea([1, 2, 1]) == 2
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

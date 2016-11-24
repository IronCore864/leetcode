class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # we need a left wall and a right wall to trap some water
        # initially set left wall and right wall to starting point
        left = 0
        right = 0
        sum = 0
        i = 1

        while i < len(height):
            # if no right wall is selected, it means we are still trying to search for the left wall
            # if the current wall is higher than the previous one, the previous wall cannot be a left wall
            # search until the current wall is lower than the previous wall, so the previous one is the selected left wall
            if right == 0 and height[i] >= height[left]:
                left = i
                i += 1
                continue

            # after we selected the left wall, search for the right wall
            # in this case the current wall is lower than the left wall so potentially it could be used to save water
            # begin from the left wall to the end, find the right wall, which could be either:
            #   a. the max height wall, if it's lower than the left wall
            #      such as 4 0 0 3 0 2
            #      4 is left wall then 3 is the right wall
            #   b. from the left wall, the next wall which is higher than the left wall
            #      such as 4 0 0 5 0 6
            #      4 is left wall then 5 is the right wall
            # and use it as right wall
            max_height_from_i = 0
            for j in range(i, len(height)):
                if height[j] >= max_height_from_i:
                    max_height_from_i = height[j]
                    right = j
                    if height[j] >= height[left]:
                        break

            # if the right wall is right next to the left wall it means there's no space between for water
            # in this case reset left and right wall and continue searching for a new left wall
            if right == left + 1:
                left = right
                i = right + 1
                right = 0
                continue

            # if there are some space indeed between the left and the right, calculate the water volumn and add it to sum
            # here the barrel effect applies: how many water can there be trapped between the left and right wall depends on which wall is shorter
            min_height = min(height[left], height[right])
            for j in range(left + 1, right):
                sum += min_height - height[j] if min_height >= height[j] else 0

            # continue searching for a new left wall and accumulate the newly trapped water
            left = right
            i = right + 1
            right = 0
        return sum


s = Solution()
print s.trap([2, 0, 2])
print s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])


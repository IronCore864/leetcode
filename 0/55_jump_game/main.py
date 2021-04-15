class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # pos marks the left most index, where it can reach to the end of the array
        # the last element can reach itself,even its value is zero
        # so, we initialize pos as len(nums)-1
        pos = len(nums)-1

        # searching backwards
        # if the current i can reach pos, the current index can reach the end of the array
        # so we can move the pos backward to current index i
        # we continue searching backward
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= pos:
                pos = i

        # if in the end, the pos is zero, it means you can reach the end from the start
        return pos == 0


if __name__ == '__main__':
    s = Solution()

    jump = [2, 3, 1, 1, 4]
    assert s.canJump(jump) == True

    jump = [3, 2, 1, 0, 4]
    assert s.canJump(jump) == False

    jump = [0, 2, 3]
    assert s.canJump(jump) == False

    jump = [1, 2, 0, 1]
    assert s.canJump(jump) == True

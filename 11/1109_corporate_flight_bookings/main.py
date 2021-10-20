from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n

        for start, end, seats in bookings:
            diff[start-1] += seats
            if end < n:
                diff[end] -= seats

        res = [0] * n
        res[0] = diff[0]
        for i in range(1, n):
            res[i] = res[i-1] + diff[i]

        return res


if __name__ == '__main__':
    # https://labuladong.gitee.io/algo/2/19/49/
    # diff array: used for frequent operations over a section of an array

    nums = [8, 2, 6, 3, 1]
    N = len(nums)

    # building the diff array
    diff = [0] * N
    diff[0] = nums[0]
    for i in range(1, N):
        diff[i] = nums[i] - nums[i - 1]

    print(diff)  # [8, -6, 4, -3, -2]

    # if you wish to add 3 on nums[i:j+1]: diff[i] += 3 then diff[j+1] -= 3
    # example: nums[1:4] add 3:
    diff[1] += 3
    diff[4] -= 3
    print(diff)  # [8, -3, 4, -3, 1]

    # recover nums from diff:
    new_nums = [0] * N
    new_nums[0] = diff[0]
    for i in range(1, N):
        nums[i] = diff[i] + nums[i-1]
    print(nums)  # [8, 5, 9, 6, 1]

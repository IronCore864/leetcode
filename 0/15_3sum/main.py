from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        negative = [num for num in nums if num < 0]
        positive = [num for num in nums if num > 0]
        zero = [0 for num in nums if num == 0]

        negative_set, positive_set = set(negative), set(positive)

        # if there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        # i.e. (-3, 0, 3) = 0
        if zero:
            for num in positive_set:
                if -num in negative_set:
                    res.add((-num, 0, num))

        # if there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(zero) >= 3:
            res.add((0, 0, 0))

        # for all pairs of negative numbers (-3, -1), check to see if their complement (4)
        # exists in the positive number set
        for i in range(len(negative)):
            for j in range(i+1, len(negative)):
                target = -(negative[i]+negative[j])
                if target in positive_set:
                    res.add(tuple(sorted([negative[i], negative[j], target])))

        # for all pairs of positive numbers (1, 1), check to see if their complement (-2)
        # exists in the negative number set
        for i in range(len(positive)):
            for j in range(i+1, len(positive)):
                target = -(positive[i]+positive[j])
                if target in negative_set:
                    res.add(tuple(sorted([positive[i], positive[j], target])))

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))

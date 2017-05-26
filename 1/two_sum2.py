class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j, n = 0, 1, len(numbers)
        while True:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                j += 1
                if j == n:
                    i += 1
                    j = i + 1
                    continue

                while numbers[j] == numbers[j - 1]:
                    j += 1
                    if j == n:
                        i += 1
                        j = i + 1
            else:
                i += 1
                while numbers[i] == numbers[i - 1]:
                    i += 1
                j = i + 1

s = Solution()
print s.twoSum([5, 25, 75], 100)

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
            print(n, first, second)
        return False


s = Solution()
print(s.increasingTriplet([1, 2, 3, 4, 5]))
print(s.increasingTriplet([5, 4, 3, 2, 1]))
print(s.increasingTriplet([5, 4, 1, 2, 3]))
print(s.increasingTriplet(range(100000)[::-1]))
print(s.increasingTriplet([1] * 100000))
print(s.increasingTriplet([5, 1, 5, 5, 2, 3, 4]))

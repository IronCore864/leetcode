class Solution:
    def mergesort(self, enum, smaller):
        half = len(enum) // 2
        if half:
            left = self.mergesort(enum[:half], smaller)
            right = self.mergesort(enum[half:], smaller)
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum

    def countSmaller(self, nums):
        smaller = [0] * len(nums)
        self.mergesort(list(enumerate(nums)), smaller)
        return smaller


# [2, 1, 1, 0]
s = Solution()
print(s.countSmaller([5, 2, 6, 1]))

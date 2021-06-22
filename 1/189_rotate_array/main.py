class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotate(self, nums: List[int], k: int) -> None:
        # Let n = 7n=7 and k = 3k=3.
        # Original List                   : 1 2 3 4 5 6 7
        # After reversing all numbers     : 7 6 5 4 3 2 1
        # After reversing first k numbers : 5 6 7 4 3 2 1
        # After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

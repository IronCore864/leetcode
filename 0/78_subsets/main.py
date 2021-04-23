class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []

        res = []
        n = len(nums)

        # for each element in the list, we can either use it, or not use it, to generate a result
        # so, there are 2^n number of results
        # path records used elements
        # iterate over the list, for each element, either use it, or not use it, and use depth to keep track of the index
        # when reaching to the end of the list, generate a result, then backtrack
        def dfs(path, depth):
            if depth == n:
                # deepcopy
                res.append(path[:])
                return

            # doesn't use current number
            dfs(path, depth+1)
            path.append(nums[depth])
            # use current number
            dfs(path, depth+1)
            # backtracking
            path.pop()

        dfs([], 0)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))

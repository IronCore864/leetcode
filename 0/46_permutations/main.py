class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        # keep a record of already used numbers, so that there is no no duplicated numbers
        used = set()

        def dfs_backtracking(path=[]):
            if len(path) == len(nums):
                res.append(path)
                return

            for num in nums:
                if num not in used:
                    used.add(num)
                    dfs_backtracking(path+[num])
                    # backtracking
                    used.remove(num)

        dfs_backtracking()
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))

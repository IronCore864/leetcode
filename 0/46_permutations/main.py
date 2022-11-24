from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        used = set()

        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
                return
            for num in nums:
                if num not in used:
                    used.add(num)
                    dfs(path+[num])
                    used.remove(num)

        dfs([])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))

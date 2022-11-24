from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        if len(digits) == 0:
            return res

        self.dfs(digits, 0, d, '', res)
        return res

    def dfs(self, nums, index, d, path, res):
        if index >= len(nums):
            res.append(path)
            return

        string1 = d[nums[index]]
        for i in string1:
            self.dfs(nums, index+1, d, path + i, res)


if __name__ == '__main__':
    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits))

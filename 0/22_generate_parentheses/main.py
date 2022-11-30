from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path, left, right):
            if len(path) == n*2:
                res.append(path)
                return

            if left < n:
                dfs(path+'(', left+1, right)
            if left > right:
                dfs(path+')', left, right+1)

        dfs('', 0, 0)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(3))

class Solution:
    def is_valid(self, result):
        balance = 0
        for c in result:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def dfs_backtracking(path=''):
            if len(path) == 2*n:
                if self.is_valid(path):
                    result.append(path)
                return

            path += '('
            dfs_backtracking(path)
            path = path[0:len(path)-1]

            path += ')'
            dfs_backtracking(path)

        def dfs_backtracking_optimized(path='', left=0, right=0):
            # skip invalid results
            if len(path) == 2*n:
                result.append(path)
                return

            # only add left parenthesis when left < n
            # for example, if n == 2, ((() will apparently be not valid
            if left < n:
                path += '('
                dfs_backtracking_optimized(path, left+1, right)
                path = path[0:len(path)-1]

            # only add right parenthesis when left >right
            # for example, if n == 2, ())) will apparently be not valid
            if left > right:
                path += ')'
                dfs_backtracking_optimized(path, left, right+1)

        # dfs_backtracking()
        dfs_backtracking_optimized()
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))

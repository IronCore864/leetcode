class Solution:
    def numTrees(self, n: int) -> int:
        res = [1] * 20

        if n == 1:
            return 1

        res[2] = 2

        for i in range(3, 20):
            s = 0
            for j in range(i):
                l, r = j, i-j-1
                s += res[l] * res[r]
            res[i] = s

        return res[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3))

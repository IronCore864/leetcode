from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        previous = 0
        for x in range(num + 1):
            if x == 0:
                res[x] = 0
            elif x == 1:
                res[x] = 1
            else:
                if x & (x - 1) == 0:
                    res[x] = 1
                    previous = x
                else:
                    res[x] = res[previous] + res[x - previous]
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(16))

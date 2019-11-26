class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l, r, u, d = 0, 0, 0, 0
        for c in moves:
            if c == "L":
                l += 1
            if c == "R":
                r += 1
            if c == "U":
                u += 1
            if c == "D":
                d += 1
        return l==r and u==d

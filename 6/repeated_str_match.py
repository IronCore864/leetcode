class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for c in B:
            if c not in A:
                return -1

        res = len(B) // len(A)
        if B in A * res:
            return res
        elif B in A * (res + 1):
            return res + 1
        elif B in A * (res + 2):
            return res + 2
        else:
            return -1

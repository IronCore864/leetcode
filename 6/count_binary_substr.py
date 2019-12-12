class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        m = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        l = list(m)
        return sum(min(a, b) for a, b in zip(l, l[1:]))


s = Solution()
print(s.countBinarySubstrings("00110"))
print(s.countBinarySubstrings("00110011"))

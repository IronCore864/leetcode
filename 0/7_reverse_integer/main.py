class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        sign = '-' if s[0] == '-' else ''
        s = s[1:] if s[0] == '-' else s
        res_str = sign + s[::-1]
        reversedInt = int(res_str)
        return reversedInt if (-1)*2**31 < reversedInt < (2**31-1) else 0

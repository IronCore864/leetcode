class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(s.strip())

        if len(s) == 0:
            return 0

        sign = -1 if s[0] == '-' else 1
        s = s[1:] if s[0] in ['-', '+'] else s

        res, i = 0, 0
        while i < len(s) and s[i].isdigit():
            res = res*10 + ord(s[i]) - ord('0')
            i += 1

        return max(-2**31, min(sign * res, 2**31-1))


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("  -0012a42"))
    print(s.myAtoi("-123"))

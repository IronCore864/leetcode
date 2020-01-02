class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        for c in str:
            if 65 <= ord(c) <= 90:
                res.append(chr(ord(c) + 32))
            else:
                res.append(c)
        return ''.join(res)

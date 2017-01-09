class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        char_map = {str(unichr(c)): 0 for c in range(128)}
        for c in t:
            char_map[c] += 1
        counter = len(t)
        d = 2 ** 32 - 1
        begin, end = 0, 0
        head = 0
        while end < len(s):
            if char_map[s[end]] > 0:
                counter -= 1
            char_map[s[end]] -= 1
            end += 1

            while counter == 0:
                if end - begin < d:
                    head = begin
                    d = end - begin
                if char_map[s[begin]] == 0:
                    counter += 1
                char_map[s[begin]] += 1
                begin += 1

        return "" if d == 2 ** 32 - 1 else s[head:head + d]


s = Solution()
print s.minWindow(
    "ADOBECODEBANC",
    "ABC"
)

print s.minWindow(
    "A",
    "A"
)

print s.minWindow(
    "AA",
    "A"
)
print s.minWindow(
    "A",
    "AA"
)

print s.minWindow(
    "ABBBBBBBBBBBC",
    "ABC"
)

print s.minWindow(
    "ABC",
    "DEF"
)

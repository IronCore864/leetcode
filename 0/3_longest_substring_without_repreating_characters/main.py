class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, start = 0, 0
        last_pos = {}

        for i, c in enumerate(s):
            if c in last_pos and start <= last_pos[c]:
                start = last_pos[c] + 1
            else:
                res = max(res, i - start + 1)

            last_pos[c] = i

        return res


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring('abcabcbb') == 3
    assert s.lengthOfLongestSubstring('bbbbb') == 1
    assert s.lengthOfLongestSubstring('pwwkew') == 3
    assert s.lengthOfLongestSubstring('tmmzuxt') == 5
    assert s.lengthOfLongestSubstring('') == 0
    assert s.lengthOfLongestSubstring(' ') == 1

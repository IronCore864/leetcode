class Solution(object):
    def longest_substr(self, s):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        char_map = {str(unichr(c)): 0 for c in range(128)}
        counter = 0
        d = 0
        begin, end = 0, 0

        while end < len(s):
            if char_map[s[end]] > 0:
                counter += 1
            char_map[s[end]] += 1
            end += 1

            while counter > 1:
                if char_map[s[begin]] > 1:
                    counter -= 1
                char_map[s[begin]] -= 1
                begin += 1
                d = max(d, end - begin)
        return d


s = Solution()
print s.longest_substr("CABCDEA")

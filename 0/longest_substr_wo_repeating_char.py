class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0

        start = 0
        end = 0

        pos_dict = {}
        maxlen = 0

        while(end < len(s)):
            if s[end] in pos_dict:
                if pos_dict[s[end]] >= start:
                    maxlen = max(maxlen, end - start)
                    start = pos_dict[s[end]] + 1
            pos_dict[s[end]] = end
            end += 1
        return max(maxlen, end - start)

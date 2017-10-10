from collections import defaultdict


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or len(s) == 0 or not p or len(p) == 0 or len(p) > len(s):
            return []

        result = []

        charsCount = defaultdict(int)
        for c in p:
            charsCount[c] += 1

        counter = len(charsCount)

        begin, end = 0, 0

        while end < len(s):
            if s[end] in charsCount:
                charsCount[s[end]] -= 1
                if charsCount[s[end]] == 0:
                    counter -= 1

            end += 1

            while counter == 0:
                if s[begin] in charsCount:
                    charsCount[s[begin]] += 1
                    if charsCount[s[begin]] > 0:
                        counter += 1

                if end - begin == len(p):
                    result.append(begin)

                begin += 1

        return result

s = Solution()
print(s.findAnagrams('abca', 'ac'))
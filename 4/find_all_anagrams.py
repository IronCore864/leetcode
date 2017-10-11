from collections import Counter


class Solution(object):
    def findAnagrams(self, hay, needle):
        """
        :type hay: str
        :type needle: str
        :rtype: List[int]
        """
        if not hay or len(hay) == 0 or not needle or len(needle) == 0 or len(needle) > len(hay):
            return []

        chars_count = Counter(needle)

        start = 0
        end = len(needle)

        for c in hay[start:end]:
            if c in chars_count:
                chars_count[c] -= 1
        zero_counter = len(chars_count) - sum([1 for i in chars_count.values() if i == 0])

        res = []

        for start in range(len(hay) - len(needle) + 1):
            end = start + len(needle)

            if zero_counter == 0:
                res.append(start)

            if hay[start] in chars_count:
                chars_count[hay[start]] += 1
                if chars_count[hay[start]] == 1:
                    zero_counter += 1
                if chars_count[hay[start]] == 0:
                    zero_counter -= 1

            if start != len(hay) - len(needle) and hay[end] in chars_count:
                chars_count[hay[end]] -= 1
                if chars_count[hay[end]] == 0:
                    zero_counter -= 1
                if chars_count[hay[end]] == -1:
                    zero_counter += 1

        return res


s = Solution()
print(s.findAnagrams("abacbabc", "abc"))

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # two words a and b are anagrams if:
        # sort string a and b, and the results are the same
        # or
        # count all letters in a and b, and the counters are equal
        # sorting is O(nlogn) but counting is O(n)

        result = defaultdict(list)

        for word in strs:
            count = [0]*26

            for c in word:
                count[ord(c)-ord('a')] += 1

            result[tuple(count)].append(word)

        return result.values()


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

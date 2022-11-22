from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match = 0

        for val in zip(*strs):
            if len(set(val)) == 1:
                match += 1
            else:
                break

        return strs[0][:match]

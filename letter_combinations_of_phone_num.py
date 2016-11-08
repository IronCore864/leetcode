class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        if '0' in digits or '1' in digits:
            return []

        digit_to_char_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = ['']

        for d in digits:
            tmpres = []
            for i in range(len(res)):
                for ch in digit_to_char_map[d]:
                    tmpres.append(res[i] + ch)
            res = tmpres
        return res


s = Solution()
s.letterCombinations('234')


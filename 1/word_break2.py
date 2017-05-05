class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not wordDict:
            return []

        memo = dict()
        memo[""] = [""]

        def sentences(txt):
            if txt not in memo:
                memo[txt] = [w + (p and ' ' + p)
                             for w in wordDict
                             if txt[0:len(w)] == w
                             for p in sentences(txt[len(w):])]
                # memo[txt] = []
                # for w in wordDict:
                #     if txt[0:len(w)] == w:
                #         if len(w) == len(txt):
                #             memo[txt].append(w)
                #         else:
                #             rest = sentences(txt[len(w):])
                #             if rest:
                #                 for p in rest:
                #                     memo[txt].append(w + " " + p)
            return memo[txt]

        return sentences(s)


s = Solution()
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
# ["cats and dog", "cat sand dog"]
print s.wordBreak("a", [])
# []
print s.wordBreak("a", ["b"])
# []

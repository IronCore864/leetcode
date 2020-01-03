class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        result = ""
        possible = [""]
        for word in words:
            if word[:-1] in possible:
                possible.append(word)
                if len(word) > len(result):
                    result = word
        return result

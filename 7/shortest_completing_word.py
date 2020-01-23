from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        license_lower = licensePlate.lower()
        license_letter_only = ""
        for c in license_lower:
            if 'a' <= c <= 'z':
                license_letter_only += c
        license_counter = Counter(license_letter_only)

        res = 'x' * 15
        for w in words:
            word_counter = Counter(w)
            match = True
            for k in license_counter:
                if k not in word_counter or word_counter[k] < license_counter[k]:
                    match = False
                    break
            if match and len(w) < len(res):
                res = w
        return res


s = Solution()
print(s.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]))

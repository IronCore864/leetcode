class Solution:
    def nextGreatestLetter(self, letters, target):
        if letters[-1] <= target:
            return letters[0]

        start, end = 0, len(letters) - 1
        while start <= end:
            mid = (end - start) // 2 + start
            if target < letters[mid]:
                if mid == 0 or target >= letters[mid - 1]:
                    return letters[mid]
                end = mid - 1
            else:
                if mid + 1 < len(letters) and target < letters[mid + 1]:
                    return letters[mid + 1]
                start = mid + 1


s = Solution()
print(s.nextGreatestLetter(["c", "f", "j"], "a"))
print(s.nextGreatestLetter(["c", "f", "j"], "c"))
print(s.nextGreatestLetter(["c", "f", "j"], "d"))
print(s.nextGreatestLetter(["c", "f", "j"], "g"))
print(s.nextGreatestLetter(["c", "f", "j"], "j"))
print(s.nextGreatestLetter(["c", "f", "j"], "k"))

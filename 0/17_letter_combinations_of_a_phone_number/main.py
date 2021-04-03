class Solution:
    def __init__(self):
        self.keys = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    # straightforward solution, easier to understand
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == '':
            return []

        results = ['']

        for digit in digits:
            new_results = []
            for word in results:
                for char in self.keys[digit]:
                    new_results.append(word+char)
            results = new_results

        return results

    # backtrack solution
    def letter_combo_backtrack(self, digits: str) -> list[str]:
        results = []
        if digits == '':
            return results

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                results.append("".join(path))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = self.keys[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        backtrack(0, [])
        return results


if __name__ == '__main__':
    s = Solution()

    digits = "23"
    print(s.letterCombinations(digits))
    print(s.letter_combo_backtrack(digits))

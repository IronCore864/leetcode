class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        # word a has only one character, not possbile to swap two
        # or word a and b have different lengths
        if len(a) == 1 or len(a) != len(b):
            return False

        # if word a and be are exactly the same
        # only possilbe swap is to do it on two identical characters
        if a == b:
            # turn word a into a set of characters (removing duplicates)
            # if the length of the set is less than the length of a, it means a has duplicated chars
            return True if len(set(a)) < len(a) else False

        # count and take note of the index of all diffrent characters in a and b
        diff = []
        for i in range(len(a)):
            if a[i] != b[i]:
                diff.append(i)
            # if more than 2 chars are different between a and b
            if len(diff) > 2:
                return False

        # a and b has only two indices where the chars are different
        # and swaping these two creates b
        return True if len(diff) == 2 and a[diff[0]] == b[diff[1]] and a[diff[1]] == b[diff[0]] else False


if __name__ == '__main__':
    s = Solution()
    assert s.buddyStrings('abcd', 'cbad') == True
    assert s.buddyStrings('ab', 'ba') == True
    assert s.buddyStrings('ab', 'ab') == False
    assert s.buddyStrings('aa', 'aa') == True
    assert s.buddyStrings('aaaaaaabc', 'aaaaaaacb') == True
    assert s.buddyStrings('abcd', 'cbad') == True

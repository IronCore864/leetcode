class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j = 0, 0  # pointer for matching, i for string and j for pattern
        k, l = len(s), 0  # pointer for back tracking *
        while i < len(s):
            if j < len(p) and p[j] == '*':
                k, l = i, j  # record the location of latest *
                j += 1  # * can match empty string
            elif j < len(p) and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif k < len(s):  # if match fails, backtracking to latest *
                i, j = k + 1, l + 1
                k += 1
            else:  # if no stars to fall back to
                return False

        # To address if pattern p is trailed by multiple stars
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)


s = Solution()
print s.isMatch('aa', 'a')
print s.isMatch('aa', 'aa')
print s.isMatch('aaa', 'aa')
print s.isMatch('aa', '*')
print s.isMatch('aa', 'a*')
print s.isMatch('ab', '?*')
print s.isMatch('aab', 'c*a*b')
print s.isMatch('', '*')
print s.isMatch('b', '?*?')
print s.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b")
print s.isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa",
                "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****")


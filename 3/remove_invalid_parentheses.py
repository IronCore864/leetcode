class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0

        level = {s}
        while True:
            valid_set = set(filter(isvalid, level))
            if valid_set:
                return list(valid_set)
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}


s = Solution()
print(s.removeInvalidParentheses("()())()"))  # ["()()()", "(())()"]
print(s.removeInvalidParentheses("(a)())()"))  # ["(a)()()", "(a())()"]
print(s.removeInvalidParentheses(")("))  # [""]

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    p = stack.pop()
                    if p + c not in ['()', '[]', '{}']:
                        return False
                    else:
                        pass

        if len(stack) == 0:
            return True
        else:
            return False


s = Solution()
print s.isValid('')
print s.isValid('()')
print s.isValid('(){}[]')
print s.isValid('{[()]}')
print s.isValid('(()')


class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True

        while '#,#' in preorder:
            start = preorder.find('#,#') - 2
            if start < 0:
                break
            end = start + 5
            while start >= 0 and preorder[start] != ',':
                start -= 1
            start += 1
            preorder = preorder[0:start] + '#' + preorder[end:]

        return preorder == '#'


s = Solution()
print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
print(s.isValidSerialization("1,#"))
print(s.isValidSerialization("9,#,#,1"))
print(s.isValidSerialization("1,#,#,#"))
print(s.isValidSerialization("9,#,92,#,#"))

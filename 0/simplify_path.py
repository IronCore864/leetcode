class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        places = [p for p in path.split("/") if p != "." and p != ""]
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)


s = Solution()
print s.simplifyPath("/.")
print s.simplifyPath("/./")
print s.simplifyPath("/../")
print s.simplifyPath("/home/")
print s.simplifyPath("/a/./b/../../c/")
print s.simplifyPath("/a/./b/../../../../c/d/")

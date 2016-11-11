class Solution(object):
    def generateParenthesis(self, n):
        result  = []
        left = 0
        right = 0
        self.helper(result, "", left, right, n)
        return result
    
    def helper(self, result, branch, left, right, n):
        if len(branch) == n * 2:
            result.append(branch)
    
        if left < n:
            self.helper(result, branch + "(", left + 1, right, n)
    
        if right < left:
            self.helper(result, branch + ")", left, right + 1, n)

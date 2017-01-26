class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x==0:
            return True
        else:
            div = 1
            while x / div >= 10:
                div *= 10
            while x != 0:
                left = x / div
                right = x % 10
        
                if left != right:
                    return False 
                x = (x % div) / 10
                div /= 100
            return True

s = Solution()
print s.isPalindrome(-123)
print s.isPalindrome(0)
print s.isPalindrome(121)

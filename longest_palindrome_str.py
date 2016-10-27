class Solution(object):
    def preProcess(self, s):
        return '#' + '#'.join(s) + '#'

    def getRes(self, s):
        return ''.join(s.split('#'))
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        T = self.preProcess(s)

        P = [None] * len(T)
        P[0] = 0

        C = 0
        R = 0
        for i in range(1, len(T)):
            im = C - (i - C)
            if R <= i:
                P[i] = 0
            else:
                P[i] = min(R - i, P[im])

            while i-1-P[i]>=0 and i + 1 + P[i]<len(T) and  T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C = i;
                R = i + P[i]

        maxlen = 0
        centerindex = 0
        for i in range(1, len(T)-1):
            if P[i] > maxlen:
                maxlen = P[i]
                centerindex = i

        return self.getRes(T[centerindex-maxlen:centerindex+maxlen+1])
            

s = Solution()
print s.longestPalindrome("aba")
print s.longestPalindrome("abcba")
print s.longestPalindrome("abccba")
print s.longestPalindrome("abcde")
print s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")

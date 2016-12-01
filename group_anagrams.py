class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for str in strs:
            str_l = [c for c in str]
            str_l.sort()
            str_sorted = ''.join(str_l)
            res.setdefault(str_sorted, []).append(str)
        return res.values()


s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


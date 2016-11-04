class Solution(object):
    def get_index_of_max_common_prefix(self, min_len_str, strs):
        res = 0
        for i in range(len(min_len_str)):
            for str in strs:
                if str[i] != min_len_str[i]:
                    return i
        return len(min_len_str) + 1

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if '' in strs:
            return ''

        min_len = 2 ** 31 - 1
        min_len_str = ''
        for str in strs:
            if len(str) < min_len:
                min_len_str = str
                min_len = len(str)
        res = self.get_index_of_max_common_prefix(min_len_str, strs)
        return min_len_str[0:res]

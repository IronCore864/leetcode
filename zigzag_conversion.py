class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < 2: return s
        
        rows = ["" for i in range(numRows)]
        i = -1
        incr = 1
        for ch in s:
            i = i + incr
            rows[i] += ch
            if i == numRows-1:
                incr = -1
            else:
                if i == 0:
                    incr = 1
        return "".join(rows)

s = Solution()
print s.convert("oxjpkcpdekyazevyzxudsirvddoxmptaodryfhdltcmuijsigolaxevcimbwduwrzqrhxvssxgmhpgpxvdyujvwrhzpktmdvcvcbquvpbhwsposktsecncwxbljxznsdiugaqbprknmabekwwrzltxixiuwihonrkutaviuixgibkuxinythvcgewcofsbycxrctbydyelzqhzyvxsetwkzuonbgqziosmjvnmtrzvkiuidrcjkavlwjaxrrybhsqsndghwhegpyrvrvgcwcpsnqsfjqgqjykwbqfyzjeojxlbtsfpwujjkbqtuzldxxbznjxmuddedqhwioneiwqvygqufezdbacrlbfggkmjbvfjjsqtrgormhlulkxombfyengkxuwypdkyyarpiiiwptqcdnsrqypunxfkrdlggvggxaxhifdzyuddjvvcvkwikdvbggkpbqvyqvfaakzzgecsazuxmqgwwbxchhtkarkqmrrmbsnixsczrwwdoebkfzpoikyibkbpbuedmrnllpkfnjkbnmovnfjxpkitwjiydmdrgqdthpywyjzmvnhksshkepdbylbdaexiwabfrabqlaegqnskhzumpzpplqvnwsvsuwxlyabjchruujhclbqcbhtozobviypcwmoxoriqbanvluzyxpaawwovkrsvrhxotnnjhvcivpfjjfjgwkhtgxqsrjpiqnymclvlhxveobpxgzgclnxtmqndzdmrsmduybifadlpebomaurljoewerzfwnxoacjydrfeuqvbtjnteegnvmjbgljcygraicamvfspynsrwgnamvqjiblomuqlcjnkloygvsytfqneycglxwwfyhtkdmxhvlujbspwlnqsefwchdpezmmzvfkbtjirwcaxxpukfmcltznaefgdtsdqaprvacmxemubeoljcquvpjxvqeajwfcyutuvvgscv", 918)
print s.convert("PAYPALISHIRING", 3) 

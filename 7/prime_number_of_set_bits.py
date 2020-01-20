class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def is_prime(num):
            return True if num in [2,3,5,7,11,13,17,19] else False
        
        res = 0
        for num in range(L, R+1):
            if is_prime(sum([1 if ch == "1" else 0 for ch in "{0:b}".format(num)])):
                res += 1
        
        return res
            

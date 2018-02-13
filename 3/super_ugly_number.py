from copy import deepcopy


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1

        ugly = [0] * n
        ugly[0] = 1
        idx = [0] * len(primes)
        val = deepcopy(primes)

        for i in range(1, n):
            ugly[i] = min(val)

            for j in range(len(primes)):
                if ugly[i] == val[j]:
                    idx[j] += 1
                    val[j] = ugly[idx[j]] * primes[j]

        return ugly[-1]


s = Solution()
print(s.nthSuperUglyNumber(12,
                           [2, 7, 13, 19]))

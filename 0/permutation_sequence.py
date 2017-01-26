from math import factorial as f


class Solution(object):
    def get_perm_helper(self, n, k, arr):
        if n == 1:
            return str(arr[0])
        total = f(n)
        num_of_same_first_digit = total / n
        first_num_idx = k / num_of_same_first_digit
        remaining_idx = k % num_of_same_first_digit
        first_num = arr[first_num_idx]
        arr.remove(first_num)
        return str(first_num) + self.get_perm_helper(n - 1, remaining_idx, arr)

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return self.get_perm_helper(n, k - 1, [_ for _ in range(1, n + 1)])


s = Solution()
print s.getPermutation(3, 1)
print s.getPermutation(3, 6)

for i in range(1, f(4) + 1):
    print s.getPermutation(4, i)

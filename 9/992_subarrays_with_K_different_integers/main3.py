from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: 'List[int]', K: 'int') -> 'int':
        """
        More generically:

        exactly(k) = at_most(k) - at_most(k-1)

        Because at_most(k) is easier to think about and easier to implement.

        Other similar sliding window questions from LeetCode:
        https://leetcode.com/problems/minimum-size-subarray-sum/
        https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
        https://leetcode.com/problems/fruit-into-baskets/
        https://leetcode.com/problems/binary-subarrays-with-sum/
        https://leetcode.com/problems/max-consecutive-ones-iii/
        https://leetcode.com/problems/replace-the-substring-for-balanced-string/
        https://leetcode.com/problems/count-number-of-nice-subarrays/
        https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
        
        A good explanation in Chinese:
        https://blog.csdn.net/qq_17550379/article/details/87292206
        """

        return self.at_most(nums, K) - self.at_most(nums, K - 1)

    def at_most(self, nums, K):
        """
        When len(dict) > K:
            removing nums[i] until len(dict) == K

        [1, 2, 1, 2, 3]
         i     j

        For each j:
        [1, 2, 1], and [2, 1] are sub-arrays with maximum K different integers ending at nums[j].

        The number equals to j - i + 1.
        """
        count = defaultdict(int)
        i, j, res = 0, 0, 0
        for j in range(len(nums)):
            count[nums[j]] += 1

            while len(count) > K:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    del count[nums[i]]
                i += 1

            res += j - i + 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.at_most([1, 2, 1, 2, 3], 2))
    # print(s.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
